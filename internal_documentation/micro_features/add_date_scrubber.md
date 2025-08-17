# Add Date Scrubber

The date scrubber has a method called `add_scrubber` that does the following:

## Purpose
Allows users to register custom date format patterns that aren't included in the built-in supported formats.


## Behavior
1. **Validates the regex pattern**: Checks if the provided regex is syntactically valid
2. **Validates the example**: Ensures the regex actually matches the provided example
3. **Stores the custom scrubber**: Adds the pattern to the internal `_custom_scrubbers` list
4. **Throws exceptions**: If regex is invalid or doesn't match the example

## Usage Example
```python
DateScrubber.add_scrubber("2023-Dec-25", r"\d{4}-[A-Za-z]{3}-\d{2}")
```

## Integration
Custom scrubbers are automatically included when calling `get_scrubber_for()`
You can clear the scrubbers by calling `DateScrubber._clear_custom_scrubbers()`





