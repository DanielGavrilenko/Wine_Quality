This web application employs a neural network to predict the quality of red wine based on user-input parameters, yielding a predicted quality score ranging from 0 to 10.

## Project Overview

The project comprises three integral parts:

1) [Prediction application](https://github.com/DanielGavrilenko/wine-quality/tree/main/Prediction-app)
2) [Api-service](https://github.com/DanielGavrilenko/wine-quality/tree/main/Api-service)
3) [Front-end](https://github.com/DanielGavrilenko/wine-quality/tree/main/front-end)

This component involves training a neural network using a dataset sourced from [ UCI Machine Learning Repository. ](https://archive.ics.uci.edu/dataset/186/wine+quality).The dataset is split into two sections, with the first part utilized for training and the second for evaluating prediction accuracy. Employing the TensorFlow library, the neural network model features two layers, one output layer, Adam optimizer, and Mean Squared Error loss function.

The API service handles both POST and GET API requests. The POST method receives parameters for a new prediction request, downloads the trained model, predicts the outcome, and stores the result in the database. The GET method facilitates retrieving comprehensive information about past requests. The application is initiated by running the "application.py" file.

The user interface of the web application is created using [Next.js](https://nextjs.org/docs) To access the webpage, execute the command "npm run dev" and open [http://localhost:3000](http://localhost:3000) in your browser to view and interact with the predicted wine quality results.
