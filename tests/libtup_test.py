import unittest
from libtup import *
from libsmp import SmpMessage, SmpValue, SmpType
from parameter import Parameter
from input import Input


class TestLibtup(unittest.TestCase):
    def setUp(self):
        pass

    def test_init_ack(self):
        self.assertEqual(
                    SmpMessage(TupMessage.ACK.value),
                    tup_message_init_ack()
                )
        message = SmpMessage(TupMessage.ACK.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT32,
                    TupMessage.CMD_GET_SENSOR_VALUE.value
                ))
        self.assertEqual(
                    message,
                    tup_message_init_ack(TupMessage.CMD_GET_SENSOR_VALUE)
                )

    def test_init_error(self):
        self.assertEqual(
                    SmpMessage(TupMessage.ERROR.value),
                    tup_message_init_error()
                )
        message = SmpMessage(TupMessage.ERROR.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT32,
                    TupMessage.CMD_GET_SENSOR_VALUE.value
                ))
        self.assertEqual(
                    message,
                    tup_message_init_error(TupMessage.CMD_GET_SENSOR_VALUE)
                )

    def test_init_load(self):
        message = SmpMessage(TupMessage.CMD_LOAD.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x42
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT16,
                    0x4242
                ))
        self.assertEqual(tup_message_init_load(0x42, 0x4242), message)

    def test_init_bind(self):
        message = SmpMessage(TupMessage.CMD_BIND_EFFECT.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x42
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x25
                ))
        self.assertEqual(tup_message_init_bind(0x42, 0x25), message)

    def test_init_play(self):
        message = SmpMessage(TupMessage.CMD_PLAY.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x25
                ))
        self.assertEqual(tup_message_init_play(0x25), message)

    def test_init_stop(self):
        message = SmpMessage(TupMessage.CMD_STOP.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x25
                ))
        self.assertEqual(tup_message_init_stop(0x25), message)

    def test_init_get_version(self):
        self.assertEqual(
                    SmpMessage(TupMessage.CMD_GET_VERSION.value),
                    tup_message_init_get_version()
                )

    def test_init_get_buildinfo(self):
        self.assertEqual(
                    SmpMessage(TupMessage.CMD_GET_BUILDINFO.value),
                    tup_message_get_buildinfo()
                )

    def test_init_set_parameters(self):
        parameters = [
            Parameter(5, 0x42),
            Parameter(10, 0x25)
        ]
        message = SmpMessage(TupMessage.CMD_SET_PARAMETER.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x25  # Id of effect
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    5  # Id 1
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT32,
                    0x42  # parameter 1
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    10  # Id 2
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT32,
                    0x25  # parameter 2
                ))

        self.assertEqual(
                    message,
                    tup_message_init_set_parameter(
                        0x25,
                        parameters
                    )
                )

    def test_init_set_input(self):
        inputs = [
            Input(5, 0x42),
            Input(10, -42)
        ]
        message = SmpMessage(TupMessage.CMD_SET_INPUT_VALUE.value)
        message.addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    0x12  # Id of effect
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    5  # Id 1
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_INT32,
                    0x42  # parameter 1
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_UINT8,
                    10  # Id 2
                )).addValue(SmpValue(
                    SmpType.SMP_TYPE_INT32,
                    -42  # parameter 2
                ))

        self.assertEqual(
                    message,
                    tup_message_init_set_input(
                        0x12,
                        inputs
                    )
                )


if __name__ == '__main__':
    unittest.main()
