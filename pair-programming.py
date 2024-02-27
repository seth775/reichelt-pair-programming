{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cd80036f-1d0f-4bc8-8f1e-515aceb3bf19",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 feet and 3 inches is equal to 1.6001999999999998 meters.\n"
     ]
    }
   ],
   "source": [
    "def convert_to_meters(feet, inches):\n",
    "    \"\"\"\n",
    "    Convert measurements in feet and inches to meters.\n",
    "    \n",
    "    Parameters:\n",
    "    feet (int, float): The feet part of the measurement.\n",
    "    inches (int, float): The inches part of the measurement.\n",
    "    \n",
    "    Returns:\n",
    "    float: The measurement in meters.\n",
    "    \n",
    "    Example:\n",
    "    >>> convert_to_meters(5, 3)\n",
    "    1.6002\n",
    "    \"\"\"\n",
    "    \n",
    "    total_inches = 12 * feet + inches\n",
    "    meters = total_inches * 0.0254\n",
    "    return meters\n",
    "\n",
    "### Example usage:\n",
    "feet = 5\n",
    "inches = 3\n",
    "print(f\"{feet} feet and {inches} inches is equal to {convert_to_meters(feet, inches)} meters.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "817f16ad-7b8a-4b96-8743-f7a248841b3b",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
