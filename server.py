from flask import Flask, request, jsonify
from stockfish import Stockfish

app = Flask(__name__)

stockfish = Stockfish(path="/usr/games/stockfish")

@app.post("/bestmove")
def bestmove():
    data = request.get_json()
    fen = data.get("fen")
    depth = data.get("depth", 8)   # default depth = 8

    if not fen:
        return jsonify({"error": "FEN required"}), 400

    stockfish.set_fen_position(fen)
    stockfish.update_engine_parameters({"Depth": depth})

    move = stockfish.get_best_move()

    return jsonify({
        "bestmove": move,
        "depth": depth
    })

@app.get("/")
def health():
    return "Working", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
