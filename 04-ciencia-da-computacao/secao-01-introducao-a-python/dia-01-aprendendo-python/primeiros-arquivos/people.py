import area

PEOPLE_PER_SQUARE_METER = 2  # number of people per square meter
FIELD_LENGTH = 60  # meters
FIELD_WIDTH = 45  # meters
people_at_concert = (
    area.rectangle(FIELD_LENGTH, FIELD_WIDTH) * PEOPLE_PER_SQUARE_METER
)
print("Our concert have about", people_at_concert, "people.")
