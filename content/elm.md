# Compile simple elm app #

Jump when you are not ready !

We did first

    elm init

it created src folder and couple of json files

Then we added a Homepage.elm in src folder.

    module Homepage exposing (main)
    
    import Html exposing (..)
    
    main = 
    text "hello!"

After this we ran the elm make as follows :

    elm make src/Homepage.elm --output Homepage.js

This created Homepage.js alongside src folder.

Then we added index.html file manually next to Homepage.js

    <html> 
    <head>    
    </head>
	    <body>
		    <div id="elm_element"></div>
		    <script src="Homepage.js"></script>
		    <script>
		    var app = Elm.Homepage.init({
		      node: document.getElementById ("elm_element")  
		    });
		    </script>
	    </body>
    </html>


---------------------------------
value and functions

value = value 
function = way to transform values  - values passed to function are called arguments 

functions from List module = List.isEmpty names

----------------------------------
view : Model -> Html msg

means view takes a model and returns an HTML which is capable of producing messages of message type.
in other words view takes a model and returns html (capable of producing messages)
read view as "html view of model"

model : 

model is just a model

update : Msg -> model -> 

means update takes a message of type message along with model and returns updated model
in other words read update as "update model". 

-----------------------------

module Main exposing (..)

.. means we are exposing everything in the modules.

We can choose to expose only certain functions. 

 
The functions we import from Hrml module like "begineeerProgram, button, div etc" are functions. they dont do anything they just return a value. button , div and text are functions which take set of arguments for attributes and return a virtual representation of what that markup might be.

Html.Events onClick function will take a message type I want to trigger and give me an attribute I can put in an element

always 4 things: 

2 values : 

1. initialModel 

2. type Msg : you can call it whatever like action etc.

then we write 2 functions 

1.update msg model - takes msg and model -> return the new model based on business logic


2. view model - takes model and returns markup.

Elm always looks for an entry point called main. You have to pass a program value. Program value is what describes how our program functions. 


-----------------CSS

https://github.com/monty5811/postcss-elm-tailwind

http://elm-bootstrap.info/

 ------

So conceptually, every function accepts one argument. It may return another function that accepts one argument. Etc. At some point it will stop returning functions.


-------------------

List.map : (a -> b) -> List a -> List b

map takes function and a list. 

Elm also uses the convention that the data structure is always the last argument across the ecosystem. This means that functions are usually designed with this possible usage in mind, making this a pretty common technique.

Partial application 

Html Message : 

div[]
    [
            button [] [text "-"]
        ,   text (String.fromInt model)
        ,   button [] [text "+"] 
    ]
    
div [] [button [] [...] ] 

First argument in div (and button) function represents attibutes to div and second argument represents list of nested elements. 



