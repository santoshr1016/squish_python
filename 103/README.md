# 103 - Simple Flask Project 

This project provides RESTful API for Planets Python

I have used https://mailtrap.io to send mail, Awesome tool
## Example

```python
@app.route('/register', methods=['POST'])
@app.route('/login', methods=['POST'])
@app.route('/get_password/<string:email>', methods=['GET'])
@app.route('/planet', methods=["POST"])
@app.route('/planets', methods=['GET'])
@app.route('/planet/<int:planet_id>', methods=["GET"])
@app.route('/planet/<int:planet_id>', methods=["PUT"])
@app.route('/planet/<int:planet_id>', methods=["DELETE"])

# Flask cli commands
flask db_create
flask db_drop
flask db_seed
```

## Development

See `requirements.txt` for package requirements
and `requirements-dev.txt` for development requirements.


## Project

https://github.com/santoshr1016/


# License
