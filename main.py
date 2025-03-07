#!/usr/bin/env python3

import os
import sys
import argparse
from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2.generic import RectangleObject

def add_margins(input_path, margin_top=72, margin_bottom=72):
    """
    Add top and bottom margins to each page of a PDF file.

    Args:
        input_path (str): Path to the input PDF file
        margin_top (int): Size of top margin in points (72 points = 1 inch)
        margin_bottom (int): Size of bottom margin in points (72 points = 1 inch)

    Returns:
        str: Path to the output PDF file
    """
    # Generate output filename
    base_name, ext = os.path.splitext(input_path)
    output_path = f"{base_name}_elongated{ext}"

    # Open the input PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Process each page
    for page in reader.pages:
        # Get original page dimensions
        original_width = page.mediabox.width
        original_height = page.mediabox.height

        # Calculate new page height with margins
        new_height = original_height + margin_top + margin_bottom

        # Create a new page with increased height
        page.mediabox = RectangleObject([
            0,  # x1 (left)
            0,  # y1 (bottom)
            original_width,  # x2 (right)
            new_height,  # y2 (top)
        ])

        # Move content down to create top margin
        op = Transformation().translate(0, margin_bottom)
        page.add_transformation(op)

        # Add the modified page to the output PDF
        writer.add_page(page)

    # Save the output PDF
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Created elongated PDF: {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Add top and bottom margins to PDF pages."
    )
    parser.add_argument(
        "input_file",
        help="Path to the input PDF file"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=72,
        help="Top margin in points (72 points = 1 inch)"
    )
    parser.add_argument(
        "--bottom",
        type=int,
        default=72,
        help="Bottom margin in points (72 points = 1 inch)"
    )

    args = parser.parse_args()

    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        sys.exit(1)

    # Process the PDF
    add_margins(args.input_file, args.top, args.bottom)

if __name__ == "__main__":
    main()