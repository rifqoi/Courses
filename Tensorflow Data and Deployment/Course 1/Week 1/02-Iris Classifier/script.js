const tf = require('@tensorflow/tfjs');
const csvUrl = './iris.csv';
const trainingData = tf.data.csv(csvUrl, {
	columnConfigs: {
		species: {
			isLabel: true
		}
	}
});

// const numOfFeatures = (await trainingData.columnNames()).length - 1;
// const numOfSamples = 150;
const convertedData =
	trainingData.map(({ xs, ys }) => {
		return { xs: Object.values(xs), ys: Object.values(ys) };
	})

console.log('bruh')
console.log(convertedData)
console.log(trainingData)
