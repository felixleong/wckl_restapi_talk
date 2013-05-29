=================
REST(ful) API 101
=================

Seh Hui, Leong |br| May 2013, Webcamp KL

.. figure:: /_static/5840311104_3ea1f9bbc3_b.jpg
    :class: fill

    CC-BY-NC-SA http://www.flickr.com/photos/rpenalozan/5840311104/

Data, Data Everywhere!
======================

.. figure:: /_static/8464661409_32aa7a26a6_b.jpg
    :class: fill

    CC-BY-SA http://www.flickr.com/photos/frauhoelle/8464661409/

RESTful is AWESOME!
===================

.. figure:: /_static/4960389917_1d0b48f117_b.jpg
    :class: fill

    CC http://www.flickr.com/photos/mccun934/4960389917/

REST-what?
==========

- REpresentational State Transfer
- **Paradigm/Infrastructure pattern to designing easy-to-understand APIs**
    - Both machine- and **programmer-readable** without convoluted protocols
- Usually called **RESTful** because no one seems to agree what a perfect REST service is

Making the Perfect Bread and Bacon
==================================

- Thinking in **resources**
- **Uniform Resource Identifier/Locator (URI/URL)**
- **HTTP**: The perfect **uniform interface**

HTTP: The Perfect Fit (I)
=========================

You can represent CRUD actions using **HTTP verbs**

:**Create**: POST
:**Retrieve**: GET
:**Update**: UPDATE
:**Delete**: DELETE

HTTP: The Perfect Fit (II)
==========================

You can get status of your requests using **HTTP status codes**

==== ================================
Code Meaning
==== ================================
200  OK
201  Created
204  No-Content (i.e. return void)
400  Bad Request
401  Unauthorized
403  Forbidden
404  Not Found
500  Internal Server Error (OMG BUG!)
==== ================================

HTTP: The Perfect Fit (III)
===========================

You can use **HTTP headers** to specify operating parameters of a transaction.

============== ==========================
Request header Description
============== ==========================
Accept         Content we want to request
Authorization  Authentication credentials
============== ==========================

=============== =============================================
Response header Description
=============== =============================================
Status          Status of the transaction 
Location        The destination URI (important for redirects)
=============== =============================================

HTTP: It's AWESOME!
===================

.. figure:: /_static/2226367161_bf288a00c9_b.jpg
    :class: fill

    CC-BY-NC-ND http://www.flickr.com/photos/frauhoelle/8464661409/

[DEMO] REST in Action
=====================

.. figure:: /_static/3541396771_551b4a34ce_b.jpg
    :class: fill

    CC-BY http://www.flickr.com/photos/cabfablab/3541396771/

Let's Get Complex
=================

.. figure:: /_static/4008887_2456af3345_o.jpg
    :class: fill

    CC-SA http://www.flickr.com/photos/hive/4008887/

Checkout Example (1)
====================

Create a new checkout cart
    
:Request: **POST** /api/v1/cart/
:Response:

    Status: 201 Created |br|
    Location: /api/v1/cart/12345/

Checkout Example (2)
====================

Add items to cart

:Request: **POST** /api/v1/cart/12345/item/
:POST Data:

    .. code:: json

        {
            "item": "/api/v1/product/milk/",
            "quantity": 2
        }

:Response:

    Status: 201 Created |br|
    Location: /api/v1/cart/12345/item/1/

Checkout Example (3)
====================

Check shopping cart contents

:Request: **GET** /api/v1/cart/12345/
:Response:

    Status: 200 OK

    .. code:: json

        {
            "time_created": "2013-05-22T08:45Z",
            "items": [
                {
                    "product": {
                        "name": "Fresh Milk",
                        "slug": "milk",
                        "price": 5.3,
                        "resource_uri": "/api/v1/product/milk/"
                    },
                    "quantity": 2,
                    "time_added": "2013-05-22T08:52Z"
                }
            ],
            "gross_total": 10.6,
            "currency": "MYR"
        }

Checkout Example (4)
====================

Update quantity of item in cart

:Request: **PUT** /api/v1/cart/12345/item/1/
:PUT data:

    .. code:: json

        { "quantity": 3 }

:Response: Status: 204 No-Content

Checkout Example (5)
====================

Checkout and make payment **(over-simplified version)**

:Request: **POST** /api/v1/cart/12345/checkout/
:POST data:

    .. code:: json

        {
            "shipping": {
                "name": "John Doe",
                "address": { "street": "…" },
                "phone": "+601222200000"
            },
            "payment": {
                "type": "CC",
                "details": { "card_number": "…" }
            }
        }

:Response:

    Status: 303 See Other |br|
    Location: /api/v1/order/320/

You Are Now Smarter!
====================

.. figure:: /_static/6966069023_5512204921_b.jpg
    :class: fill

    CC-BY http://www.flickr.com/photos/sylvainkalache/6966069023/

You Have Learned…
=================

- We are in the **Data Age**
- REST(ful) API and its **components**
- Why **HTTP is a godsend**
- How do you interact with a **REST(ful) service**

Parting Gift
============

**Code, Demo, Presentation**

http://github.com/felixleong/wckl_restapi_talk/

**Contact Details**

:Email: felixleong@gmail.com
:Facebook: http://facebook.com/leongsh/
:Twitter: http://twitter.com/felixleong/

References
==========

- REST in Practice, *by Jim, Savas and Ian* (O'Reilly)
    - http://shop.oreilly.com/product/9780596805838.do
- RESTful Web Services Cookbook, *by Subbu Allamaraju* (O'Reilly)
    - http://shop.oreilly.com/product/9780596801694.do
    - Companion website: http://restcookbook.com/

License
=======

This work is licensed under a `Creative Commons Attribution-ShareAlike 3.0 Unported License`_.

.. _Creative Commons Attribution-ShareAlike 3.0 Unported License: http://creativecommons.org/licenses/by-sa/3.0/deed.en_US

.. DEFINITIONS

.. |br| raw:: html

    <br/>
