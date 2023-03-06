from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)
openai.api_key = "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"


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get the values entered by the user
        num1 = request.form['num1']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(num1),
            max_tokens=1024,
            n=1,
            top_p=1,
            stop=None,
            temperature=0.9
        )
        return redirect(url_for("form", result=response.choices[0].text))

    result = request.args.get("result")
    print(result)
    return render_template("form.html", result=result)

        # Add the numbers
def generate_prompt(num1):
        return """Recommend me the paticular genre movies as List?"""+num1.format(num1.capitalize())

if __name__ == '__main__':
    app.run(debug=True)
