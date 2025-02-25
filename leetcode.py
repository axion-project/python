def full_justify(words, maxWidth):
    if not words:
        return []
    
    result = []
    current_line = []
    line_length = 0
    
    i = 0
    while i < len(words):
        # Check if word is too long
        if len(words[i]) > maxWidth:
            raise ValueError(f"Word '{words[i]}' is longer than maxWidth")
            
        # Check if adding the word exceeds maxWidth
        if line_length + len(words[i]) + len(current_line) > maxWidth:
            # Handle single word case
            if len(current_line) == 1:
                result.append(current_line[0].ljust(maxWidth))
            else:
                num_spaces = maxWidth - line_length
                # Calculate spaces between words
                gaps = len(current_line) - 1
                spaces_per_gap = num_spaces // gaps
                extra_spaces = num_spaces % gaps
                
                # Build the line
                line = ""
                for j in range(len(current_line) - 1):
                    line += current_line[j]
                    spaces = spaces_per_gap + (1 if j < extra_spaces else 0)
                    line += " " * spaces
                line += current_line[-1]
                result.append(line)
            
            current_line = []
            line_length = 0
        
        current_line.append(words[i])
        line_length += len(words[i])
        i += 1
    
    # Handle the last line differently - left justify
    if current_line:
        last_line = " ".join(current_line)
        result.append(last_line.ljust(maxWidth))
    
    return result