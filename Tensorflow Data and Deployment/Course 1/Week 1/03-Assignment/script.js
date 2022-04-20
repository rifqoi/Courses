const tf = require('@tensorflow/tfjs');
const trainingUrl = './wdbc-train.csv';
//const trainingUrl = '/data/wdbc-train.csv';

// Take a look at the 'wdbc-train.csv' file and specify the column
// that should be treated as the label in the space below.
// HINT: Remember that you are trying to build a classifier that
// can predict from the data whether the diagnosis is malignant or benign.
const trainingData = tf.data.csv(trainingUrl, {
	// YOUR CODE HERE
	columnConfigs: {
		diagnosis: {
			isLabel: true
		}
	}

});

// Convert the training data into arrays in the space below.
// Note: In this case, the labels are integers, not strings.
// Therefore, there is no need to convert string labels into
// a one-hot encoded array of label values like we did in the
// Iris dataset example.
//const convertedTrainingData = // YOUR CODE HERE
const convertedTrainingData = trainingData.map(({ xs, ys }) => {
	return { xs: Object.values(xs), ys: Object.values(ys) };
}).batch(10);



const testingUrl = './wdbc-test.csv';

// Take a look at the 'wdbc-test.csv' file and specify the column
// that should be treated as the label in the space below..
// HINT: Remember that you are trying to build a classifier that 
// can predict from the data whether the diagnosis is malignant or benign.
const testingData = tf.data.csv(testingUrl, {
	columnConfigs: {
		diagnosis: {
			isLabel: true
		}
	}
});

// Convert the testing data into arrays in the space below.
// Note: In this case, the labels are integers, not strings.
// Therefore, there is no need to convert string labels into
// a one-hot encoded array of label values like we did in the
// Iris dataset example. 
const convertedTestingData = testingData.map(({ xs, ys }) => {
	return { xs: Object.values(xs), ys: Object.values(ys) };
}).batch(10);

// Specify the number of features in the space below.
// HINT: You can get the number of features from the number of columns
// and the number of labels in the training data. 
// const numOfFeatures = (trainingData.columnNames()).length - 1;

console.log(trainingData)
// console.log(convertedTestingData)
