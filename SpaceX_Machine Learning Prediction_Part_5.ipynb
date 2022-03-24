{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center>\n",
    "    <img src=\"https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png\" width=\"300\" alt=\"cognitiveclass.ai logo\"  />\n",
    "</center>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Space X  Falcon 9 First Stage Landing Prediction**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Assignment:  Machine Learning Prediction\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Estimated time needed: **60** minutes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Space X advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against space X for a rocket launch.   In this lab, you will create a machine learning pipeline  to predict if the first stage will land given the data from the preceding labs.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing\\_1.gif)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Several examples of an unsuccessful landing are shown here:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most unsuccessful landings are planed. Space X; performs a controlled landing in the oceans.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objectives\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Perform exploratory  Data Analysis and determine Training Labels\n",
    "\n",
    "*   create a column for the class\n",
    "*   Standardize the data\n",
    "*   Split into training data and test data\n",
    "\n",
    "\\-Find best Hyperparameter for SVM, Classification Trees and Logistic Regression\n",
    "\n",
    "*   Find the method performs best using test data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import Libraries and Define Auxiliary Functions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will import the following libraries for the lab\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pandas is a software library written for the Python programming language for data manipulation and analysis.\n",
    "import pandas as pd\n",
    "# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays\n",
    "import numpy as np\n",
    "# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.\n",
    "import matplotlib.pyplot as plt\n",
    "#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics\n",
    "import seaborn as sns\n",
    "# Preprocessing allows us to standarsize our data\n",
    "from sklearn import preprocessing\n",
    "# Allows us to split our data into training and testing data\n",
    "from sklearn.model_selection import train_test_split\n",
    "# Allows us to test parameters of classification algorithms and find the best one\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "# Logistic Regression classification algorithm\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "# Support Vector Machine classification algorithm\n",
    "from sklearn.svm import SVC\n",
    "# Decision Tree classification algorithm\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "# K Nearest Neighbors classification algorithm\n",
    "from sklearn.neighbors import KNeighborsClassifier"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This function is to plot the confusion matrix.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_confusion_matrix(y,y_predict):\n",
    "    \"this function plots the confusion matrix\"\n",
    "    from sklearn.metrics import confusion_matrix\n",
    "\n",
    "    cm = confusion_matrix(y, y_predict)\n",
    "    ax= plt.subplot()\n",
    "    sns.heatmap(cm, annot=True, ax = ax); #annot=True to annotate cells\n",
    "    ax.set_xlabel('Predicted labels')\n",
    "    ax.set_ylabel('True labels')\n",
    "    ax.set_title('Confusion Matrix'); \n",
    "    ax.xaxis.set_ticklabels(['did not land', 'land']); ax.yaxis.set_ticklabels(['did not land', 'landed'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Load the dataframe\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load the data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>Date</th>\n",
       "      <th>BoosterVersion</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Outcome</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2010-06-04</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>6104.959412</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2012-05-22</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>525.000000</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0005</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2013-03-01</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>677.000000</td>\n",
       "      <td>ISS</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0007</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2013-09-29</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>PO</td>\n",
       "      <td>VAFB SLC 4E</td>\n",
       "      <td>False Ocean</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1003</td>\n",
       "      <td>-120.610829</td>\n",
       "      <td>34.632093</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2013-12-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3170.000000</td>\n",
       "      <td>GTO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1004</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   FlightNumber        Date BoosterVersion  PayloadMass Orbit    LaunchSite  \\\n",
       "0             1  2010-06-04       Falcon 9  6104.959412   LEO  CCAFS SLC 40   \n",
       "1             2  2012-05-22       Falcon 9   525.000000   LEO  CCAFS SLC 40   \n",
       "2             3  2013-03-01       Falcon 9   677.000000   ISS  CCAFS SLC 40   \n",
       "3             4  2013-09-29       Falcon 9   500.000000    PO   VAFB SLC 4E   \n",
       "4             5  2013-12-03       Falcon 9  3170.000000   GTO  CCAFS SLC 40   \n",
       "\n",
       "       Outcome  Flights  GridFins  Reused   Legs LandingPad  Block  \\\n",
       "0    None None        1     False   False  False        NaN    1.0   \n",
       "1    None None        1     False   False  False        NaN    1.0   \n",
       "2    None None        1     False   False  False        NaN    1.0   \n",
       "3  False Ocean        1     False   False  False        NaN    1.0   \n",
       "4    None None        1     False   False  False        NaN    1.0   \n",
       "\n",
       "   ReusedCount Serial   Longitude   Latitude  Class  \n",
       "0            0  B0003  -80.577366  28.561857      0  \n",
       "1            0  B0005  -80.577366  28.561857      0  \n",
       "2            0  B0007  -80.577366  28.561857      0  \n",
       "3            0  B1003 -120.610829  34.632093      0  \n",
       "4            0  B1004  -80.577366  28.561857      0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv(\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv\")\n",
    "\n",
    "# If you were unable to complete the previous lab correctly you can uncomment and load this csv\n",
    "\n",
    "# data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')\n",
    "\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Flights</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Orbit_ES-L1</th>\n",
       "      <th>Orbit_GEO</th>\n",
       "      <th>Orbit_GTO</th>\n",
       "      <th>Orbit_HEO</th>\n",
       "      <th>Orbit_ISS</th>\n",
       "      <th>...</th>\n",
       "      <th>Serial_B1058</th>\n",
       "      <th>Serial_B1059</th>\n",
       "      <th>Serial_B1060</th>\n",
       "      <th>Serial_B1062</th>\n",
       "      <th>GridFins_False</th>\n",
       "      <th>GridFins_True</th>\n",
       "      <th>Reused_False</th>\n",
       "      <th>Reused_True</th>\n",
       "      <th>Legs_False</th>\n",
       "      <th>Legs_True</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>6104.959412</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>525.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>677.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.0</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3170.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>86.0</td>\n",
       "      <td>15400.000000</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>86</th>\n",
       "      <td>87.0</td>\n",
       "      <td>15400.000000</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87</th>\n",
       "      <td>88.0</td>\n",
       "      <td>15400.000000</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>88</th>\n",
       "      <td>89.0</td>\n",
       "      <td>15400.000000</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>89</th>\n",
       "      <td>90.0</td>\n",
       "      <td>3681.000000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>90 rows × 83 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    FlightNumber   PayloadMass  Flights  Block  ReusedCount  Orbit_ES-L1  \\\n",
       "0            1.0   6104.959412      1.0    1.0          0.0          0.0   \n",
       "1            2.0    525.000000      1.0    1.0          0.0          0.0   \n",
       "2            3.0    677.000000      1.0    1.0          0.0          0.0   \n",
       "3            4.0    500.000000      1.0    1.0          0.0          0.0   \n",
       "4            5.0   3170.000000      1.0    1.0          0.0          0.0   \n",
       "..           ...           ...      ...    ...          ...          ...   \n",
       "85          86.0  15400.000000      2.0    5.0          2.0          0.0   \n",
       "86          87.0  15400.000000      3.0    5.0          2.0          0.0   \n",
       "87          88.0  15400.000000      6.0    5.0          5.0          0.0   \n",
       "88          89.0  15400.000000      3.0    5.0          2.0          0.0   \n",
       "89          90.0   3681.000000      1.0    5.0          0.0          0.0   \n",
       "\n",
       "    Orbit_GEO  Orbit_GTO  Orbit_HEO  Orbit_ISS  ...  Serial_B1058  \\\n",
       "0         0.0        0.0        0.0        0.0  ...           0.0   \n",
       "1         0.0        0.0        0.0        0.0  ...           0.0   \n",
       "2         0.0        0.0        0.0        1.0  ...           0.0   \n",
       "3         0.0        0.0        0.0        0.0  ...           0.0   \n",
       "4         0.0        1.0        0.0        0.0  ...           0.0   \n",
       "..        ...        ...        ...        ...  ...           ...   \n",
       "85        0.0        0.0        0.0        0.0  ...           0.0   \n",
       "86        0.0        0.0        0.0        0.0  ...           1.0   \n",
       "87        0.0        0.0        0.0        0.0  ...           0.0   \n",
       "88        0.0        0.0        0.0        0.0  ...           0.0   \n",
       "89        0.0        0.0        0.0        0.0  ...           0.0   \n",
       "\n",
       "    Serial_B1059  Serial_B1060  Serial_B1062  GridFins_False  GridFins_True  \\\n",
       "0            0.0           0.0           0.0             1.0            0.0   \n",
       "1            0.0           0.0           0.0             1.0            0.0   \n",
       "2            0.0           0.0           0.0             1.0            0.0   \n",
       "3            0.0           0.0           0.0             1.0            0.0   \n",
       "4            0.0           0.0           0.0             1.0            0.0   \n",
       "..           ...           ...           ...             ...            ...   \n",
       "85           0.0           1.0           0.0             0.0            1.0   \n",
       "86           0.0           0.0           0.0             0.0            1.0   \n",
       "87           0.0           0.0           0.0             0.0            1.0   \n",
       "88           0.0           1.0           0.0             0.0            1.0   \n",
       "89           0.0           0.0           1.0             0.0            1.0   \n",
       "\n",
       "    Reused_False  Reused_True  Legs_False  Legs_True  \n",
       "0            1.0          0.0         1.0        0.0  \n",
       "1            1.0          0.0         1.0        0.0  \n",
       "2            1.0          0.0         1.0        0.0  \n",
       "3            1.0          0.0         1.0        0.0  \n",
       "4            1.0          0.0         1.0        0.0  \n",
       "..           ...          ...         ...        ...  \n",
       "85           0.0          1.0         0.0        1.0  \n",
       "86           0.0          1.0         0.0        1.0  \n",
       "87           0.0          1.0         0.0        1.0  \n",
       "88           0.0          1.0         0.0        1.0  \n",
       "89           1.0          0.0         0.0        1.0  \n",
       "\n",
       "[90 rows x 83 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')\n",
    "\n",
    "# If you were unable to complete the previous lab correctly you can uncomment and load this csv\n",
    "\n",
    "# X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_3.csv')\n",
    "\n",
    "X.head(100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a NumPy array from the column <code>Class</code> in <code>data</code>, by applying the method <code>to_numpy()</code>  then\n",
    "assign it  to the variable <code>Y</code>,make sure the output is a  Pandas series (only one bracket df\\['name of  column']).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y = data['Class'].to_numpy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  2\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Standardize the data in <code>X</code> then reassign it to the variable  <code>X</code> using the transform provided below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# students get this \n",
    "X = preprocessing.StandardScaler().fit(X).transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.71291154e+00, -1.94814463e-16, -6.53912840e-01, ...,\n",
       "        -8.35531692e-01,  1.93309133e+00, -1.93309133e+00],\n",
       "       [-1.67441914e+00, -1.19523159e+00, -6.53912840e-01, ...,\n",
       "        -8.35531692e-01,  1.93309133e+00, -1.93309133e+00],\n",
       "       [-1.63592675e+00, -1.16267307e+00, -6.53912840e-01, ...,\n",
       "        -8.35531692e-01,  1.93309133e+00, -1.93309133e+00],\n",
       "       ...,\n",
       "       [ 1.63592675e+00,  1.99100483e+00,  3.49060516e+00, ...,\n",
       "         1.19684269e+00, -5.17306132e-01,  5.17306132e-01],\n",
       "       [ 1.67441914e+00,  1.99100483e+00,  1.00389436e+00, ...,\n",
       "         1.19684269e+00, -5.17306132e-01,  5.17306132e-01],\n",
       "       [ 1.71291154e+00, -5.19213966e-01, -6.53912840e-01, ...,\n",
       "        -8.35531692e-01, -5.17306132e-01,  5.17306132e-01]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We split the data into training and testing data using the  function  <code>train_test_split</code>.   The training data is divided into validation data, a second set used for training  data; then the models are trained and hyperparameters are selected using the function <code>GridSearchCV</code>.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  3\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the function train_test_split to split the data X and Y into training and test data. Set the parameter test_size to  0.2 and random_state to 2. The training data and test data should be assigned to the following labels.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<code>X_train, X_test, Y_train, Y_test</code>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "we can see we only have 18 test samples.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(18,)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  4\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a logistic regression object  then create a  GridSearchCV object  <code>logreg_cv</code> with cv = 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "parameters ={\"C\":[0.01,0.1,1],'penalty':['l2'], 'solver':['lbfgs']}# l1 lasso l2 ridge\n",
    "lr=LogisticRegression()\n",
    "\n",
    "logreg_cv = GridSearchCV(lr, parameters, cv=10).fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We output the <code>GridSearchCV</code> object for logistic regression. We display the best parameters using the data attribute <code>best_params\\_</code> and the accuracy on the validation data using the data attribute <code>best_score\\_</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tuned hpyerparameters :(best parameters)  {'C': 0.01, 'penalty': 'l2', 'solver': 'lbfgs'}\n",
      "accuracy : 0.8464285714285713\n"
     ]
    }
   ],
   "source": [
    "print(\"tuned hpyerparameters :(best parameters) \",logreg_cv.best_params_)\n",
    "print(\"accuracy :\",logreg_cv.best_score_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  5\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate the accuracy on the test data using the method <code>score</code>:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8333333333333334"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "logreg_cv.score(X_test, Y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets look at the confusion matrix:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "yhat=logreg_cv.predict(X_test)\n",
    "plot_confusion_matrix(Y_test,yhat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examining the confusion matrix, we see that logistic regression can distinguish between the different classes.  We see that the major problem is false positives.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  6\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a support vector machine object then  create a  <code>GridSearchCV</code> object  <code>svm_cv</code> with cv - 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "parameters = {'kernel':('linear', 'rbf','poly','rbf', 'sigmoid'),\n",
    "              'C': np.logspace(-3, 3, 5),\n",
    "              'gamma':np.logspace(-3, 3, 5)}\n",
    "svm = SVC()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "svm_cv = GridSearchCV(svm, parameters, cv=10).fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tuned hpyerparameters :(best parameters)  {'C': 1.0, 'gamma': 0.03162277660168379, 'kernel': 'sigmoid'}\n",
      "accuracy : 0.8482142857142856\n"
     ]
    }
   ],
   "source": [
    "print(\"tuned hpyerparameters :(best parameters) \",svm_cv.best_params_)\n",
    "print(\"accuracy :\",svm_cv.best_score_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  7\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate the accuracy on the test data using the method <code>score</code>:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8333333333333334"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "svm_cv.score(X_test, Y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can plot the confusion matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "yhat=svm_cv.predict(X_test)\n",
    "plot_confusion_matrix(Y_test,yhat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  8\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a decision tree classifier object then  create a  <code>GridSearchCV</code> object  <code>tree_cv</code> with cv = 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "parameters = {'criterion': ['gini', 'entropy'],\n",
    "     'splitter': ['best', 'random'],\n",
    "     'max_depth': [2*n for n in range(1,10)],\n",
    "     'max_features': ['auto', 'sqrt'],\n",
    "     'min_samples_leaf': [1, 2, 4],\n",
    "     'min_samples_split': [2, 5, 10]}\n",
    "\n",
    "tree = DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "tree_cv = GridSearchCV(tree, parameters, cv=10).fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tuned hpyerparameters :(best parameters)  {'criterion': 'entropy', 'max_depth': 18, 'max_features': 'sqrt', 'min_samples_leaf': 4, 'min_samples_split': 10, 'splitter': 'random'}\n",
      "accuracy : 0.8875000000000002\n"
     ]
    }
   ],
   "source": [
    "print(\"tuned hpyerparameters :(best parameters) \",tree_cv.best_params_)\n",
    "print(\"accuracy :\",tree_cv.best_score_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  9\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate the accuracy of tree_cv on the test data using the method <code>score</code>:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7777777777777778"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tree_cv.best_estimator_.score(X_test, Y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GridSearchCV(cv=10, estimator=DecisionTreeClassifier(),\n",
       "             param_grid={'criterion': ['gini', 'entropy'],\n",
       "                         'max_depth': [2, 4, 6, 8, 10, 12, 14, 16, 18],\n",
       "                         'max_features': ['auto', 'sqrt'],\n",
       "                         'min_samples_leaf': [1, 2, 4],\n",
       "                         'min_samples_split': [2, 5, 10],\n",
       "                         'splitter': ['best', 'random']})"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tree_cv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7777777777777778"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tree_cv.score(X_test, Y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can plot the confusion matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "yhat = tree_cv.predict(X_test)\n",
    "plot_confusion_matrix(Y_test,yhat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  10\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a k nearest neighbors object then  create a  <code>GridSearchCV</code> object  <code>knn_cv</code> with cv = 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\n",
    "              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],\n",
    "              'p': [1,2]}\n",
    "\n",
    "KNN = KNeighborsClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "knn_cv = GridSearchCV(KNN, parameters, cv=10).fit(X_train, Y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tuned hpyerparameters :(best parameters)  {'algorithm': 'auto', 'n_neighbors': 10, 'p': 1}\n",
      "accuracy : 0.8482142857142858\n"
     ]
    }
   ],
   "source": [
    "print(\"tuned hpyerparameters :(best parameters) \",knn_cv.best_params_)\n",
    "print(\"accuracy :\",knn_cv.best_score_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  11\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate the accuracy of tree_cv on the test data using the method <code>score</code>:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8333333333333334"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn_cv.score(X_test, Y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can plot the confusion matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "yhat = knn_cv.predict(X_test)\n",
    "plot_confusion_matrix(Y_test,yhat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TASK  12\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Find the method performs best:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = ['logistic regression', 'support vector machine', 'decision tree classifier', 'k nearest neighbors']\n",
    "score = [logreg_cv.score(X_test, Y_test), svm_cv.score(X_test, Y_test), tree_cv.score(X_test, Y_test), knn_cv.score(X_test, Y_test)]\n",
    "\n",
    "result_df = pd.DataFrame(data={'Model':model, 'Accuracy Score':score})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Model'>"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlMAAAE9CAYAAAAvV+dfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAmTklEQVR4nO3de7xVdZ3/8deHc1S8ZV7IMS7KFFqOQhpgFkMW3mgyNJ28pelM8rOH1tRv+k3WmJn1m8lJpyk1kcxoqp+YkyKj5CXN+w1URFFpSB090SSKN1RE4PP7Y61z2G724ezDOsAGX8/Hgwd7rfXda3/2Xmt/93t/1zprR2YiSZKkNdNvfRcgSZK0ITNMSZIkVWCYkiRJqsAwJUmSVIFhSpIkqQLDlCRJUgXt6+uBd9hhh9xll13W18NLkiQ17b777ns2Mwc0WrbewtQuu+zCrFmz1tfDS5IkNS0i/ru7ZR7mkyRJqsAwJUmSVIFhSpIkqYL1ds6UJEkbqzfeeIOOjg6WLFmyvktRL/Xv359BgwaxySabNH0fw5QkSX2so6ODrbfeml122YWIWN/lqEmZyXPPPUdHRwdDhw5t+n4e5pMkqY8tWbKE7bff3iC1gYkItt9++16PKBqmJElaCwxSG6Y12W6GKUmSNlJXXnklEcFjjz22vkvptRUrVvCFL3yBPfbYgz333JNRo0bxxBNPrO+yGvKcKUmS1rJvfvObfbq+b3zjG021u/TSSxkzZgxTp07lzDPP7NMaai1fvpy2trY+Xedll13GggULmDNnDv369aOjo4Mtt9yy0jqXLVtGe3vfRx9HpiRJ2ggtXryYO+64gx//+MdMnTq1a/7y5cv58pe/zJ577snw4cM577zzAJg5cyYf/OAHGTFiBKNHj+bll19mypQpnHrqqV33/fjHP87NN98MwFZbbcUZZ5zBPvvsw1133cVZZ53FqFGj2GOPPZg4cSKZCcD8+fPZf//9GTFiBHvvvTe///3vOe6447jqqqu61nvssccyffr0N9X/xz/+kZ122ol+/YqoMmjQILbddlsArr32Wvbee29GjBjBuHHjAFi0aBGHHnoow4cP5wMf+ABz5swB4Mwzz2TixIkceOCBHH/88SxcuJDDDz+cUaNGMWrUKO64447Kr7UjU5IkbYSmTZvGwQcfzK677sp2223H/fffz957783kyZN54okneOCBB2hvb2fRokUsXbqUI488kssuu4xRo0bx0ksvsfnmm692/a+88gp77LEHZ511FgC77747Z5xxBgDHHXccV199NYcccgjHHnssp512GocddhhLlixhxYoVfPazn+V73/seEyZM4MUXX+TOO+/kpz/96ZvW/6lPfYoxY8Zw2223MW7cOD796U+z1157sXDhQk466SRuvfVWhg4dyqJFi4BitG6vvfZi2rRp3HTTTRx//PHMnj0bgPvuu4/bb7+dzTffnGOOOYYvfelLjBkzhqeeeoqDDjqIRx99tNJrbZii74dfNxbNDiO/1bi/rMp9RVq3FixY0GObn/zkJ5x00kksWLCA8ePH86Mf/Yivf/3rXH311Rx33HE888wzXW0feOABtt9+ewYOHNi17sWLF/P888/zyiuvdM1bsmQJzz77LAsWLKCtrY199923a9k111zDhRdeyGuvvcYLL7zA4MGD2W233XjqqafYZ5993lTzsGHDeOyxx5gzZw4zZszgoIMOelM9AP369WPevHncdNNN3HTTTYwbN47LL7+cV199lbFjx3ZdumC77bYD4Pbbb+dXv/oVAB/96Ed57rnnePHFFwH4xCc+0RUOf/Ob3/DII490Pc5LL73Eyy+/zNZbb92LLfBmhilJkjYyixYt4s4772TevHlEBMuXLyciOP3007sOv9XKzIZ/xdbe3s6KFSu6pl9//fWu25tttlnXeVJLlizha1/7GjNmzGDgwIGce+65vP766w0fq9Phhx/OFVdcwfTp0zn33HMbttlss80YP34848ePZ8cdd2TatGkccMABDWtt9Fid7WrPtVqxYgV33XVXjyNvveE5U5IkbWSuueYaDj/8cO69917uueceZs2axZAhQ7j33nsZO3YsP/vZz1i2bBkAzz//PO9+97v505/+1HVYbPHixSxbtozBgwczd+5cVqxYwR/+8Ieu5fU6Q9Z2223HK6+8wjXXXAPA1ltvzU477cS1117b1e61114DisN4F198MQC77bbbKut86KGHukazVqxYwZw5c9h5553Zd999ueWWW7r+sq/zMN/YsWP5xS9+AcDNN9/MDjvswNve9rZV1nvggQdy/vnnd01395x6w5EpSZI2MldddRWnnHLKm+Z97GMf48orr+Tb3/42jz/+OPvvvz/t7e0ce+yxnHjiiVx44YWcfvrp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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "result_df.plot.bar(x='Model', y='Accuracy Score', color=['gray', 'gray', 'lightgray', 'gray'], figsize=(10,5), rot=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Authors\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change Log\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "| Date (YYYY-MM-DD) | Version | Changed By    | Change Description      |\n",
    "| ----------------- | ------- | ------------- | ----------------------- |\n",
    "| 2021-08-31        | 1.1     | Lakshmi Holla | Modified markdown       |\n",
    "| 2020-09-20        | 1.0     | Joseph        | Modified Multiple Areas |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Copyright © 2020 IBM Corporation. All rights reserved.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
