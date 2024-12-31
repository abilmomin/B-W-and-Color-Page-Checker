import fitz  # PyMuPDF
import numpy as np

def is_color_page(img_array):
    """
    Determine if a page is color or black and white.
    Returns True if color, False if black and white/grayscale.
    """
    # If image is not RGB, it's definitely black and white
    if len(img_array.shape) < 3:
        return False
    
    # Check if all RGB channels are equal (indicating grayscale)
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    
    # Allow for small variations due to compression
    threshold = 30
    is_gray = np.allclose(r, g, atol=threshold) and np.allclose(g, b, atol=threshold)
    
    # Also check if the image only contains black and white pixels
    unique_colors = len(np.unique(img_array.reshape(-1, img_array.shape[-1]), axis=0))
    is_bw = unique_colors <= 2
    
    return not (is_gray or is_bw)

def analyze_pdf(pdf_path):
    """
    Analyze a PDF file and count color vs black and white pages.
    """
    try:
        doc = fitz.open(pdf_path)
        bw_count = 0
        color_count = 0
        
        print(f"Analyzing PDF: {pdf_path}")
        print(f"Total pages: {len(doc)}")
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            pix = page.get_pixmap()
            
            # Convert to numpy array
            img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
                pix.height, pix.width, pix.n
            )
            
            if is_color_page(img_array):
                color_count += 1
                print(f"Page {page_num + 1}: Color")
            else:
                bw_count += 1
                print(f"Page {page_num + 1}: Black and White")
        
        print("\nSummary:")
        print(f"Black and White Pages: {bw_count}")
        print(f"Color Pages: {color_count}")
        print(f"Total Pages: {bw_count + color_count}")
        
        doc.close()
        return bw_count, color_count
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return 0, 0

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_pdf>")
        sys.exit(1)
    
    analyze_pdf(sys.argv[1])