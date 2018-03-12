from enum import Enum
from libsmp import SerialFrame, Frame, SmpMessage, SmpType, SmpValue
try:
    from .parameter import Parameter
    from .input import Input
except (ImportError, SystemError):
    from parameter import Parameter
    from input import Input


class TupMessage(Enum):
    ACK = 1
    ERROR = 2
    CMD_LOAD = 10
    CMD_PLAY = 11
    CMD_STOP = 12
    CMD_GET_VERSION = 13
    CMD_GET_PARAMETER = 14
    CMD_SET_PARAMETER = 15
    CMD_BIND_EFFECT = 16
    CMD_GET_SENSOR_VALUE = 17  # Deprecated
    CMD_SET_SENSOR_VALUE = 18  # Deprecated
    CMD_GET_BUILDINFO = 19
    CMD_ACTIVATE_INTERNAL_SENSORS = 20
    CMD_GET_INPUT_VALUE = 21
    CMD_SET_INPUT_VALUE = 22
    RESP_VERSION = 100
    RESP_PARAMETER = 101
    RESP_SENSOR = 102  # Deprecated
    RESP_BUILDINFO = 103
    RESP_INPUT = 104


def decode_message(message):
    if message.msgid == TupMessage.ACK.value:
        if message.getNumberOfValues() >= 1:
            value = message.getValue(0)
            print("ACK {}".format(_get_message_type(value.value)))
        else:
            print("General ACK")
    elif message.msgid == TupMessage.ERROR.value:
        if message.getNumberOfValues() >= 1:
            value = message.getValue(0)
            print("ERROR {}".format(_get_message_type(value.value)))
        else:
            print("General ERROR")
    elif message.msgid == TupMessage.RESP_VERSION.value:
        if message.getNumberOfValues() >= 1:
            value = message.getValue(0)
            print("Version : {}".format(value.value))
        else:
            print("Bad version")
    elif message.msgid == TupMessage.RESP_BUILDINFO.value:
        if message.getNumberOfValues() >= 1:
            value = message.getValue(0)
            print("Build info : \n{}".format(value.value))
        else:
            print("Bad build info")


def _get_message_type(data):
    for value in TupMessage:
        if data == value.value:
            return value
    return ""


def tup_message_init_ack(messageType=None):
    message = SmpMessage(TupMessage.ACK.value)
    if messageType is not None and isinstance(messageType, TupMessage):
        message.addValue(SmpValue(
            SmpType.SMP_TYPE_UINT32,
            messageType.value
        ))
    return message


def tup_message_init_error(messageType=None):
    message = SmpMessage(TupMessage.ERROR.value)
    if messageType is not None and isinstance(messageType, TupMessage):
        message.addValue(SmpValue(
            SmpType.SMP_TYPE_UINT32,
            messageType.value
        ))
    return message


def tup_message_init_load(bankId, effectId):
    if isinstance(effectId, int) and isinstance(bankId, int):
        if effectId >= 0 and \
                effectId <= 65535 and \
                bankId >= 0 and \
                bankId <= 255:
            message = SmpMessage(TupMessage.CMD_LOAD.value)
            message.addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        bankId
                    )).addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT16,
                        effectId
                    ))
            return message


def tup_message_init_bind(bankId, bindingFlag):
    if isinstance(bankId, int) and isinstance(bindingFlag, int):
        if 0 <= bankId <= 255 and 0 <= bindingFlag <= 255:
            message = SmpMessage(TupMessage.CMD_BIND_EFFECT.value)
            message.addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        bankId
                    )).addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        bindingFlag
                    ))
            return message


def tup_message_init_play(bankId):
    if isinstance(bankId, int):
        if 0 <= bankId <= 255:
            message = SmpMessage(TupMessage.CMD_PLAY.value)
            message.addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        bankId
                    ))
            return message


def tup_message_init_stop(bankId):
    if isinstance(bankId, int):
        if 0 <= bankId <= 255:
            message = SmpMessage(TupMessage.CMD_STOP.value)
            message.addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        bankId
                    ))
            return message


def tup_message_init_get_version():
    return SmpMessage(TupMessage.CMD_GET_VERSION.value)


def tup_message_get_buildinfo():
    return SmpMessage(TupMessage.CMD_GET_BUILDINFO.value)


def tup_message_init_set_parameter(bankId, parameters):
    if not isinstance(bankId, int):
        return

    if bankId < 0 or bankId > 255:
        return

    message = SmpMessage(TupMessage.CMD_SET_PARAMETER.value)
    message.addValue(SmpValue(SmpType.SMP_TYPE_UINT8, bankId))

    for parameter in parameters:
        if isinstance(parameter, Parameter):
            message.addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        parameter.id
                    )).addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT32,
                        parameter.value
                    ))

    return message


def tup_message_init_set_input(bankId, inputs):
    if not isinstance(bankId, int):
        return

    if bankId < 0 and bankId > 255:
        return

    message = SmpMessage(TupMessage.CMD_SET_INPUT_VALUE.value)
    message.addValue(SmpValue(SmpType.SMP_TYPE_UINT8, bankId))

    for value in inputs:
        if isinstance(value, Input):
            message.addValue(SmpValue(
                        SmpType.SMP_TYPE_UINT8,
                        value.id
                    )).addValue(SmpValue(
                        SmpType.SMP_TYPE_INT32,
                        value.value
                    ))

    return message
