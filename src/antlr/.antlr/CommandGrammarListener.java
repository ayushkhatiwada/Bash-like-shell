// Generated from /home/ayush/comp0010-shell-python-p22/src/antlr/CommandGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CommandGrammarParser}.
 */
public interface CommandGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(CommandGrammarParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(CommandGrammarParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(CommandGrammarParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(CommandGrammarParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#seq}.
	 * @param ctx the parse tree
	 */
	void enterSeq(CommandGrammarParser.SeqContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#seq}.
	 * @param ctx the parse tree
	 */
	void exitSeq(CommandGrammarParser.SeqContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(CommandGrammarParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(CommandGrammarParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#quoted}.
	 * @param ctx the parse tree
	 */
	void enterQuoted(CommandGrammarParser.QuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#quoted}.
	 * @param ctx the parse tree
	 */
	void exitQuoted(CommandGrammarParser.QuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterSingleQuoted(CommandGrammarParser.SingleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitSingleQuoted(CommandGrammarParser.SingleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#backQuoted}.
	 * @param ctx the parse tree
	 */
	void enterBackQuoted(CommandGrammarParser.BackQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#backQuoted}.
	 * @param ctx the parse tree
	 */
	void exitBackQuoted(CommandGrammarParser.BackQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterDoubleQuoted(CommandGrammarParser.DoubleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitDoubleQuoted(CommandGrammarParser.DoubleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(CommandGrammarParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(CommandGrammarParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(CommandGrammarParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(CommandGrammarParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandGrammarParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(CommandGrammarParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandGrammarParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(CommandGrammarParser.RedirectionContext ctx);
}