def reverse_text(text):
    """Reverse a given text string."""
    return text[::-1]

# Example usage
if __name__ == "__main__":
    original = "Hello, World!"
    reversed_text = reverse_text(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_text}")