def cancel_appointment(status):
    """Cancel a booked appointment and reject invalid transitions."""
    if status == "booked":
        return "Cancelled"
    elif status == "cancelled":
        return "Cannot cancel"
    else:
        return "Invalid appointment status"


if __name__ == "__main__":
    print(cancel_appointment("booked"))
