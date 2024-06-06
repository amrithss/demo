from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory list to store to do items
todo_items = []

@app.route('/')
def index():
    return render_template('index.html', todo_items=todo_items)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    todo_items.append({'title': title})
    return redirect(url_for('index'))

@app.route('/update/<int:item_id>', methods=['POST'])
def update_todo(item_id):
    if item_id < len(todo_items):
        todo_items[item_id]['title'] = request.form['title']
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_todo(item_id):
    if item_id < len(todo_items):
        del todo_items[item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
