import unittest
from app import cancel_appointment


class TestCancellation(unittest.TestCase):

    def test_booked_appointment_can_be_cancelled(self):
        self.assertEqual(cancel_appointment("booked"), "Cancelled")

    def test_cancelled_appointment_cannot_be_cancelled_again(self):
        self.assertEqual(cancel_appointment("cancelled"), "Cannot cancel")

    def test_unknown_status_is_rejected(self):
        self.assertEqual(
            cancel_appointment("unknown"),
            "Invalid appointment status"
        )


if __name__ == "__main__":
    unittest.main()
