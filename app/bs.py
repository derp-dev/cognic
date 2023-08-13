def print_file(file_path):
  with open(file_path, "r") as f:
    text = f.read()
    print(f"""
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h1>{file_path}</h1>
            <p>{text}</p>
          </div>
        </div>
      </div>
    """)

print_file("my_file.txt")

"""
This code will now print the contents of the file my_file.txt in a Bootstrap container with a heading and a paragraph
"""