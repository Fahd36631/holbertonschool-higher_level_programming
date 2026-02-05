#!/usr/bin/env python3
"""
Task 0: Creating a Simple Templating Program
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None: Creates output files or logs errors
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    
    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Handle empty template
    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        invitation = template
        
        # Replace placeholders with values or "N/A" if missing
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        
        # Handle None values
        if name is None:
            name = "N/A"
        if event_title is None:
            event_title = "N/A"
        if event_date is None:
            event_date = "N/A"
        if event_location is None:
            event_location = "N/A"
        
        # Replace placeholders in the template
        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))
        
        # Generate output file name
        output_filename = f"output_{index}.txt"
        
        # Write to output file
        try:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(invitation)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
