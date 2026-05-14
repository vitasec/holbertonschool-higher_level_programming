#!/usr/bin/python3
"""ye"""


def generate_invitations(template, attendees):
    # comment
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # comment
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # comment
    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return
    
    # comment
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # comment
    for idx, attendee in enumerate(attendees, start=1):
        # comment
        personalized_message = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )
        
        # comment
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as file:
            file.write(personalized_message)
        print(f"Invitation for attendee {idx} written to {output_filename}")
