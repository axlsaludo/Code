import ics
from datetime import datetime, timedelta
import pytz

# Create a calendar
calendar = ics.Calendar()

# Define the timezone for the events (Philippine Time)
timezone = pytz.timezone("Asia/Manila")

# Define the schedule (course name, start time, end time, weekdays)
schedule = [
    ("CPE416E - DSP - Magtibay", "07:30", "12:00", ["MO"]),
    ("CPE414E - Emerging Tech - Juanillas", "10:30", "13:30", ["TU", "TH"]),
    ("CPEL3E - CISCO - Juanillas", "14:30", "16:30", ["TU"]),
    ("CPE412 - OL - Gumapac", "16:30", "18:00", ["MO"]),
    ("TECHNO - OL - De Castro", "18:00", "19:30", ["MO"]),
    ("CPE413E - Computer Architecture and Organization - De Castro", "16:00", "19:00", ["WE"]),
    ("CPEL3L - CISCO LAB - Juanillas", "16:00", "18:00", ["TH"]),
    ("CPE415 - Thesis 1 - Ramos", "07:00", "10:00", ["SA"]),
    ("CPEIP - Fundamentals of IT - Juanillas", "10:00", "13:00", ["SA"]),
    ("CPE413L - Computer Architecture LAB - Juanillas", "13:00", "16:00", ["SA"]),
]

# Define the start date of the semester (example: August 12, 2024)
start_date = datetime(2024, 8, 12)

# Create events
for course, start_time, end_time, weekdays in schedule:
    for weekday in weekdays:
        # Calculate the first occurrence of each event
        current_date = start_date + timedelta(days=(["MO", "TU", "WE", "TH", "FR", "SA", "SU"].index(weekday)))
        event_start = timezone.localize(datetime.combine(current_date, datetime.strptime(start_time, "%H:%M").time()))
        event_end = timezone.localize(datetime.combine(current_date, datetime.strptime(end_time, "%H:%M").time()))

        # Create the event
        event = ics.Event()
        event.name = course
        event.begin = event_start
        event.end = event_end
        
        # Set the event to repeat weekly
        event.rrule = {"freq": "weekly"}
        
        # Add the event to the calendar
        calendar.events.add(event)

# Save the calendar to a .ics file
calendar_path = "CPE4A_schedule.ics"
with open(calendar_path, "w") as f:
    f.writelines(calendar.serialize_iter())

print(f"Calendar saved to {calendar_path}")
