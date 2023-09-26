# **Outfit Generator**

A website made in Django that allows you to input types of clothing, and generates an outfit from your clothing based on a couple of factors! A personal project of mine still in progress.

## **How to Use**
The website is not hosted on a server yet, so if you want to run this project on localhost, follow these steps:
1. Fork the repo
2. Open the command line and enter the repo wherever you saved it
3. Go to the /clothingSite directory and type the following: _python manage.py runserver_
4. Open a browser and go to the following URL: _http://127.0.0.1:8000/outfit-generator_

## **Current Implementation**
Currently, colour is the only factor accounted for in the algorithm. The generated outfit will consist of a mixture of neutral  and **complimentary** colours (colours opposite in the colour wheel). In the future, the algorithm will also generate **monochromatic** (same hue different saturation/shades ) and **analogous** (colours adjacent in the colour wheel) outfits.

## Future To-Do
1. Add tests to ensure the validity of the project
2. Update the UI to look more modern
3. Have the generate outfit algorithm account for the weather using a weather API(precipitation, temperature, etc)
4. Have the generate outfit algorithm account for formality and differences in fabric
