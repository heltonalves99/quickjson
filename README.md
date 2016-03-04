# QuickJSON

##### Quick and easy way to create JSON data!

# Documentation

### How to use:

1.  Add a wanted JSON structure, with specific keys and use [placeholders for values](https://github.com/heltonalves99/quickjson#list-of-valid-placeholders-for-generated-values)
2.  Choose the expiration time (hour, day or week)
3.  Click on Send!
4.  A new link is generated with your JSON data, and that's it! o/
    Now you can send a GET request on the generated link and use it as you wish.
     It will return an JSON object with your data.
     If you want an object list, just pass to URL the parameter **count**.

    **Ex:** quickjson.com/as2fcx2jk**?count=20**

### List of valid placeholders for generated values:

*   **["word"]** - create a word.
*   **["words", 1]** - create a list of words, the second parameter is the quantity of words the list must have.
*   **["url"]** - create an URL of type string.
*   **["time"]** - create a time with HH:MM:SS structure.
*   **["text"]** - create a text containing a specific quantity of caracteres.
*   **["street_name"]** - create a street name.
*   **["random_number", 3]** - create an integer random number, the second parameter is the quantity of decimal places.
*   **["name"]** - create a compound person name.
*   **["name_female"]** - create a compound female person name.
*   **["name_male"]** - create a compound male person name.
*   **["email]** - create an email.
*   **["list_email", 10]** - create a list of email, the second parameter is the quantity of emails the list must have.
*   **["year"]** - create a year with four digits (YYYY).
*   **["uuid4"]** - create an uuid4 type ID.
*   **["user_name"]** - create an user name.
*   **["url"]** - create an url of a site.
*   **["timezone"]** - create a timezone. Ex: Europe/Prague
*   **["street_address"]** - create a street address name. Ex: 500 Lossie Green
*   **["state"]** - create a state. Ex: Minnesota
*   **["slug"]** - create a slug. Ex: molestiae-autem-coisa
*   **["safe_hex_color"]** - create a color in hex format. Ex: #33ee00
*   **["rgb_color"]** - create a rgb color. Ex: 156,144,194
*   **["mime_type"]** - create a MIME type. Ex: multipart/encrypted
*   **["locale"]** - create a locale. Ex: pt_BR
*   **["month"]** - create a month number. Ex: 12
*   **["month_name"]** - create a month name. Ex: February
*   **["first_name"]** - create a first name.
*   **["first_name_female"]** - create a first female name.
*   **["first_name_male"]** -create a first male name.
*   **["file_name"]** - create a file name. Ex: optio.txt
*   **["file_extension"]** - create a file extension. Ex: .txt
*   **["day_of_week"]** - create a named day of week. Ex: Monday
*   **["day_of_month"]** - create a day number. Ex: 23
*   **["credit_card_provider"]** - create a name of credit card provider. Ex: Mastercard
*   **["credit_card_number"]** - create a credit card number. Ex: 869992095432728
*   **["country"]** - create a country name. Ex: Brazil
*   **["country_code"]** - create a country code. Ex: BR
*   **["color_name"]** - create a color name: Ex: WhiteSmoke
*   **["city"]** - create a city name. Ex: São Luis
*   **["boolean"]** - create a boolean, true or falsa.
*   **["date"]** - create a ISO formated date. Ex: 1982-07-30
*   **["from", "http://quickjson.com/generate/10c110fbba64?count=3"]** - Import another quickjson or existing json endpoint.
*   **["image", "100x100"]** - Create a URL to image through placehold.it, The parameters are the key of placeholde and size specification (ex: "200x10").
*   **["list_image", "100x100", 10]** - Create a list of URL to images through placehold.it, The parameters are the key of placeholde, size specification (ex: "200x10") and last one is a integer with the amount of images list.
