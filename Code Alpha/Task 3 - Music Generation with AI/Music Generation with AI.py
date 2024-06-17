import os
import random
import pretty_midi

def generate_random_midi(output_dir, num_notes=128, tempo=120, duration_per_note=1.0):
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create an Instrument instance
    instrument = pretty_midi.Instrument(program=0)  # Use program number 0 for piano

    # Add random notes
    time = 0
    for _ in range(num_notes):
        pitch = random.randint(60, 100)  # Random pitch between 60 and 100
        start_time = time
        end_time = start_time + duration_per_note
        note = pretty_midi.Note(
            velocity=random.randint(50, 100),  # Random velocity
            pitch=pitch,
            start=start_time,
            end=end_time
        )
        instrument.notes.append(note)
        time = end_time

    # Add the instrument to the MIDI data
    midi_data.instruments.append(instrument)

    # Write the MIDI data to a file
    midi_filename = os.path.join(output_dir, 'generated.mid')
    midi_data.write(midi_filename)

    print(f"Generated MIDI file: {midi_filename}")

# Directory to save generated MIDI file
output_directory = 'generated_music'

# Generate MIDI file
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate MIDI with default parameters
generate_random_midi(output_directory)
