# Fullstack-Project

I have created this website as a project for my Fullstack with Django module. It is an e-commerce site. I chose to do this type of application for the dual purpose of creating a site for my wife to sell her quilts on as well.

## UX

When i chose to do the e-commerce site for my project, I instantly thought of my wife's dream of selling the quilts that she makes. The target audience for the site is generally anyone looking for handmade quilts to buy

### User Stories

- As a shopper, I want to purchase a quilt as a gift.
...
- As a happy customer, I want to recieve coupons from the seller for future purchases.
...
- As a shopper, I want an easy to view layout with images of the product.
...
- As a shoper, I want to know that my purchase is secure.

Wireframes are stored in the mockups folder : (/mockups/fullstack wireframes.pdf)

### Features


## Existing Features

- Email - allows shoppers/customers to contact the seller by filling out a basic email form.
...
- Purchase - allows shoppers/customers to view and purchase available inventory by adding the item to a cart
...
- Cart - allows shoppers/customers to save products in a temporary shopping cart until ready to check-out
...
- Check-out - allows shoppers/customers to purchase the saved items in thier cart
...
- Patterns - allows shoppers/customers to upload thier own quilting patterns
...
- Subscribe - allows shoppers/customers to subscribe to a mailing list for discounts/coupons/discussion topics


## Technologies Used

### JQuery
- https://jquery.com/
The project uses JQuery to simplify DOM manipulation.

### Django
- https://www.djangoproject.com/
The project uses Django for many tasks, including dbstorage, admin functions

### Python
- https://www.python.org/
The project used Python for site creation and app management

### Bootstrap
- https://getbootstrap.com/
The project uses Bootstrap for the layout, stylings, and grid system

### AWS
- https://aws.amazon.com/
The project uses Amazon Web Services for the C9 terminal, S3 for storage, as well as IAM for user management

### Stripe
- https://stripe.com/
The project uses Stripe's payment and backend handling of the payments

## Testing

I have utilized Travis Continuous Integration testing at the following link:
[![Build Status](https://travis-ci.org/teetsjeremy/fullstack-project.svg?branch=master)](https://travis-ci.org/teetsjeremy/fullstack-project)

I also tested the responsiveness of the site using chrome dev tools, everything operated as desired at this time.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Registration form:
    1. Go to the "Register" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears

2. Login form:
    1. Go to the "Login" page
    2. Try to login with empty fields and verify that an error message appears
    3. Try to login with in-valid credentials and verify an error message appears
    4. Try to login with valid credentials and verify a success message appears

3. Cart
    1. Add item to cart and verify it is acutally placed in the "cart"
    2. Remove items from the cart and verify that the item is no longer in the "cart"
    3. Update quantities of items in the cart and verify the quanitiy actually changes


## Deployment

The project is deployed on Heroku, the github repository is linked to Heroku as well. I did not utilize the automatic build feature and elected to build the app only as I wished and not with every git push.
I stored all config vars in a hidden file within the app and simply used the cofig vars setting in heroku to add all of my needed values/keys

You can see the project here: (https://full-stack-project.herokuapp.com/)

## Credits

### Media

1. The photos used in this site were obtained from Pexels

### Acknowledgements

1. I received inspiration for this project from the ecommerce site in the learning module.