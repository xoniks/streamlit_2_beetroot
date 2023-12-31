import streamlit as st
import json
import datetime

# Load or initialize parking lot status from a JSON file
PARKING_LOTS_FILE = "parking_lots.json"

def load_parking_lots():
    try:
        with open(PARKING_LOTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {f"Lot {i + 1}": None for i in range(10)}

def save_parking_lots(parking_lots):
    with open(PARKING_LOTS_FILE, "w") as file:
        json.dump(parking_lots, file)

def reset_parking_lots():
    # Reset parking lots at 7 PM every day
    now = datetime.datetime.now()
    if now.hour == 19 and now.minute == 0 and now.second == 0:
        return {f"Lot {i + 1}": None for i in range(10)}
    return None

# Initialize parking lot status
parking_lots = load_parking_lots()

def parking_app():
    global parking_lots  # Make parking_lots a global variable

    st.title("Parking App")

    # Reset parking lots at 7 PM
    reset_result = reset_parking_lots()
    if reset_result:
        parking_lots = reset_result
        save_parking_lots(parking_lots)
        st.success("Parking lots reset at 7 PM.")

    # Sidebar to display worker information
    st.sidebar.title("Worker Information")
    worker_name = st.sidebar.text_input("Enter Worker Name", "")

    # Main content
    st.write(f"Welcome, {worker_name}!")

    # Display available parking lots
    st.subheader("Available Parking Lots")
    available_lots = [lot for lot, status in parking_lots.items() if status is None]
    selected_lot = st.selectbox("Select Parking Lot", available_lots)

    # Book parking lot
    if st.button("Book Parking Lot"):
        parking_lots[selected_lot] = worker_name
        save_parking_lots(parking_lots)
        st.success(f"{worker_name} successfully booked {selected_lot}.")

    # Display booked parking lots
    st.subheader("Booked Parking Lots")
    booked_lots = {lot: worker for lot, worker in parking_lots.items() if worker is not None}
    if not booked_lots:
        st.info("No parking lots have been booked yet.")
    else:
        for lot, worker in booked_lots.items():
            st.write(f"{lot}: Booked by {worker}")

# Run the app
if __name__ == "__main__":
    parking_app()
