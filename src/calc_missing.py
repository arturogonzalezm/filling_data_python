def calc_missing(readings):
    mercury_levels = []
    missing_indices = []

    # Parse the input readings
    for reading in readings:
        timestamp, value = reading.split('\t')
        if 'Missing' in value:
            missing_indices.append(len(mercury_levels))
            mercury_levels.append(None)
        else:
            mercury_levels.append(float(value))

    # Linear interpolation for missing values
    for i in missing_indices:
        before = after = None
        # Find the nearest non-missing value before the missing value
        for j in range(i - 1, -1, -1):
            if mercury_levels[j] is not None:
                before = mercury_levels[j]
                break

        # Find the nearest non-missing value after the missing value
        for k in range(i + 1, len(mercury_levels)):
            if mercury_levels[k] is not None:
                after = mercury_levels[k]
                break

        # Ensure both before and after have been assigned before calculating the missing value
        if before is not None and after is not None:
            estimated_value = (before + after) / 2
        elif before is not None:
            estimated_value = before  # If no after value is available, use the before value
        elif after is not None:
            estimated_value = after  # If no before value is available, use the after value
        else:
            # This else block theoretically should never be hit with valid data
            estimated_value = 0  # Default value in case of an unexpected situation

        mercury_levels[i] = estimated_value

    # Print the estimated missing values
    for i in missing_indices:
        print(f"{mercury_levels[i]:.2f}")
