import pyautogui
import time
card_number = 1001346
text_box_position = (97,764)
return_image = "return_to_search.png"
search_button_image = "search_button.png"
scroll_down_pos = (238,782)
select_card_pos = (565, 341)
load_button_image = "load_button.png"
next_button_image = "next_button.png"
print_button_image = "first_print_button_image.png"
final_print_button_image = "last_print_button.png"
click_card_pos = (667, 351)

def print_card(card_id):
    # # Click on return button
    # Find position of the return button
    return_pos = pyautogui.locateOnScreen(return_image, confidence = 0.9)
    # Click on the return button after locating it
    pyautogui.click(pyautogui.center(return_pos))
    # Wait a little bit
    time.sleep(3)
    # Scroll down by clicking bottom arrow twice so that "ID Number appears on page
    pyautogui.click(scroll_down_pos)
    time.sleep(1)
    pyautogui.click(scroll_down_pos)
    # Click where we will enter text
    pyautogui.moveTo(text_box_position)
    pyautogui.click(text_box_position)
    # Write the card number
    for i in range(8):
        pyautogui.press("backspace")
    
    pyautogui.write(str(card_id))
    
    time.sleep(2)
    # Click on search button
    search_button_pos = pyautogui.locateOnScreen(search_button_image, confidence = 0.9)
    pyautogui.click(pyautogui.center(search_button_pos))
    time.sleep(2)
    #pyautogui.moveTo(click_card_pos, duration = 2)
    pyautogui.click(click_card_pos)
    load_button_pos = pyautogui.locateOnScreen(load_button_image, confidence = 0.9)
    pyautogui.click(pyautogui.center(load_button_pos))
    time.sleep(9)
    next_button_pos = pyautogui.locateOnScreen(next_button_image, confidence = 0.9)
    pyautogui.click(pyautogui.center(next_button_pos))
    time.sleep(2)
    print_button_pos = pyautogui.locateOnScreen(print_button_image, confidence = 0.9)
    pyautogui.click(pyautogui.center(print_button_pos))
    time.sleep(2)
    final_print_button_pos = pyautogui.locateOnScreen(final_print_button_image, confidence = 0.9)
    #pyautogui.moveTo(pyautogui.center(final_print_button_pos), duration = 3)
    
    pyautogui.click(pyautogui.center(final_print_button_pos))
    time.sleep(6)
    
for i in range(1001415, 1001636):
    print("Card printing: ", i)
    print_card(i)
    
    
