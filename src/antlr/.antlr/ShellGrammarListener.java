// Generated from /Users/janp/Documents/UCL/COMP0010/comp0010-shell-python-p22/src/antlr/ShellGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ShellGrammarParser}.
 */
public interface ShellGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ShellGrammarParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ShellGrammarParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(ShellGrammarParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(ShellGrammarParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#seq}.
	 * @param ctx the parse tree
	 */
	void enterSeq(ShellGrammarParser.SeqContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#seq}.
	 * @param ctx the parse tree
	 */
	void exitSeq(ShellGrammarParser.SeqContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(ShellGrammarParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(ShellGrammarParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(ShellGrammarParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(ShellGrammarParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(ShellGrammarParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(ShellGrammarParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(ShellGrammarParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(ShellGrammarParser.RedirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#quoted}.
	 * @param ctx the parse tree
	 */
	void enterQuoted(ShellGrammarParser.QuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#quoted}.
	 * @param ctx the parse tree
	 */
	void exitQuoted(ShellGrammarParser.QuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterSingleQuoted(ShellGrammarParser.SingleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitSingleQuoted(ShellGrammarParser.SingleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterDoubleQuoted(ShellGrammarParser.DoubleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitDoubleQuoted(ShellGrammarParser.DoubleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#backQuoted}.
	 * @param ctx the parse tree
	 */
	void enterBackQuoted(ShellGrammarParser.BackQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#backQuoted}.
	 * @param ctx the parse tree
	 */
	void exitBackQuoted(ShellGrammarParser.BackQuotedContext ctx);
}