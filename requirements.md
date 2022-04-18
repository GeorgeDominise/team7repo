## Functional Requirements

1. Buy Item
2. *Add Pictures for Items
3. Sell Item
4. Login
5. Create Account
6. Bid on Item
7. Find Items
8. See All Seller's Items
9. User ratings 
10. Logout
11. Add to Cart
12. Delete Account
13.
14. 
15. 

## Non-functional Requirements

1. Expected to work on multiple browsers
2. Keep program code organized and maintainable
3. Password Requirements
4. Processing time under 1.0s

## Use Cases

0. Use Case Name (Should match functional requirement name) DO NOT EDIT THIS. IT SERVES AS EVERYONE'S TEMPLATE.
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

1.

2. Buy Item
- **Pre-condition:** The customer must be logged in.

- **Trigger:** Customer selects "Buy Item" option.

- **Primary Sequence:**

  1. System prompts the customer to enter in their card holder name, credit card number, CVV, and card expiration date. All fields are required.
  2. Customer has the option to save card information in database through a checkbox.
  3. System checks to make sure object is still available.
  4. System charges customer.
  5. Customer is shown a message confirming that the order has been placed.
  6. Customer is redirected to the home page.

- **Primary Postconditions:** The order has been placed, send an email to the seller. The customer's credit card has been charged for the transaction.

- **Alternate Sequence:**

  1. The customer fails to fill in all necessary fields.
  2. A message saying "Please fill in all required fields marked by an asterisk (*)" is flashed to the top of the screen.

3. Sell Item
- **Pre-condition:** The customer must be logged in.

- **Trigger:** Customer selects "Sell Item" option, located at the top of the page.

- **Primary Sequence:**

  1. System prompts the seller to enter in the item name*, price*, description, and an image. Required fields have an asterisk(*).
  2. Seller is redirected to the newly created item-buy page, with a flashed message that informs the seller their item is on the store.

- **Alternate Sequrence:**

  1. The seller fails to fill in all the necessary fields.
  2. A message saying "Please fill in all required fields marked by an asterisk (*)" is flashed to the top of the screen." 

4.

5. Create Account
- **Pre-condition:** The user must have an email account

- **Trigger:** User selects "Create Account" option, located under the login screen

- **Primary Sequence:**

  1. System prompts the user to enter in their preferred email and asks them to confirm it
  2. Systems promts the user to enter in a password that meets requirements and to re-type it in order to confirm
  3. User is redirected to either a welcome or home page which will show up whenever they login. They have access to improved features on the website.

- **Alternate Sequrence:**

  1. The user fails to fill in all the necessary feilds or their email/password do not meet requirements
  2. A message saying "Please fill in all required fields" or "Enter a valid email/password"

6. Bid on Item
- **Pre-condition:** The user must be logged into their account

- **Trigger:** User selects "Place Bid" option, located near where the "Buy" option is

- **Primary Sequence:**

  1. System prompts the user to enter in their preferred bid amount$
  2. Systems updates to show the latest bid amount placed$
  3. User secures item if no other user has placed a higher bid during the alotted bid time period 

- **Alternate Sequrence:**

  1. The user fails to fill in all the necessary feilds or places an insufficient bid
  2. A message saying "Please fill in all required fields" or "Enter a sufficient bid amount" 

7. Find Items
- **Pre-condition**
   The user must be logged into their account
- **Trigger**
  User selects a search bar to type the item name, at the top of the screen.
- **Primary Sequence:**
  1.System prompts the user to input the name of an item into a search bar
  2.System offers suggestions below the search bar that are close to
  what's input above.
  3.User can either press enter to find a specific item or click on the
  recommended item.

- **Alternate Sequence:**
 
  1.User inputs the name of an item and it doesn't appear on the screen.
  2.System offers alternative items that the seller provides, otherwise 
  displays not found.

8. See All Seller's Items
- **Pre-condition:**
  User is logged into their account on a seller's page.
- **Trigger:**
  User presses a button that says "Display all items" located next to search
  bar
- **Primary Sequence:**
  1. User presses the display all items button
  2. System brings the user to a page displaying all of the items offered
  by the seller.
- **Alternate Sequeunce:**
  1. The user isn't logged into their account to view the seller's items.
  2. Prompts the user to log into their account to view the items offered
  by the seller.
9. User Ratings
