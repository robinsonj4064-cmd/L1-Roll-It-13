def make_statement(statement, decoration):
    """Adds emojis / additional characters to the start and end of headings"""
    ends = decoration * 3
    print(f"{ends} {statement} {ends}")



    # Main routine
make_statement("I love Python", "🐍" )
make_statement("Round Results", "=")
