function move(board) {
   const legalMoves = board.legal_moves;
   const maxMoves = legalMoves.length - 1;
   if (
      !board.is_stalemate() &&
      !board.is_insufficient_material() &&
      maxMoves > 0
   ) {
      const randomIndex = Math.floor(Math.random() * (maxMoves + 1));
      return legalMoves[randomIndex].toString();
   }
}
