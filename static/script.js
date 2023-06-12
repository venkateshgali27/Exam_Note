// Define the correct answers
const correctAnswers = {
  question1: 'A',
  question2: 'B',
  question3: 'D',
  question4: 'D',
  question5: 'B',
  question6: 'C',
  question7: 'D',
  question8: 'A',
  question9: 'A',
  question10: 'C', 
  question11: 'C',
  question12: 'D',
  question13: 'C',
  question14: 'B',
  question15: 'D',
  question16: 'C',
  question17: 'D',
  question18: 'A',
  question19: 'D',
  question20: 'C',
  question21: 'B',
  question22: 'A',
  question23: 'B',
  question24: 'B',
  question25: 'A',
  question26: 'B',
  question27: 'D',
  question28: 'B',
  question29: 'B',
  question30: 'C',
  question31: 'B',
  question32: 'C',
  question33: 'A',
  question34: 'C',
  question35: 'B',
  question36: 'B',
  question37: 'C',
  question38: 'B',
  question39: 'B',
  question40: 'B',
  question41: 'D',
  question42: 'C',
  question43: 'D',
  question44: 'A',
  question45: 'B',
  question46: 'A',
  question47: 'D',
  question48: 'C',
  question49: 'B',
  question50: 'B',
  question51: 'D',
  question52: 'D',
  question53: 'B',
  question54: 'B',
  question55: 'C',
  question56: 'C',
  question57: 'B',
  question58: 'C',
  question59: 'B',
  question60: 'D',
};

// Function to evaluate the exam
function evaluateExam(event) {
  event.preventDefault(); // Prevent form submission

  let score = 0;

  // Evaluate each question
  Object.keys(correctAnswers).forEach(question => {
    const selectedOption = document.querySelector(`input[name=${question}]:checked`).value;

    // Check if the selected option is correct
    if (selectedOption === correctAnswers[question]) {
      score++;
    }
  });

  // Display the score
  const result = document.getElementById('result');
  result.textContent = `Your score: ${score}/${Object.keys(correctAnswers).length}`;
  result.style.display = 'block';
}
document.getElementById('examForm').addEventListener('submit', evaluateExam);
