from flask import Flask, request, jsonify
from stockfish import Stockfish

app = Flask(__name__)

# ✅ Use correct stockfish path
stockfish = Stockfish(path="/usr/games/stockfish", depth=12)
stockfish.set_skill_level(15)

@app.route("/bestmove", methods=["POST"])
def bestmove():
    data = request.get_json()
    fen = data.get("fen")

    if not fen:
        return jsonify({"error": "FEN required"}), 400

    stockfish.set_fen_position(fen)
    move = stockfish.get_best_move()

    return jsonify({"bestmove": move})

@app.get("/")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
