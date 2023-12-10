// Generated from /home/ayush/comp0010-shell-python-p22/src/antlr/ShellGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ShellGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		UNQUOTED=1, PIPE=2, SINGLE_QUOTE=3, DOUBLE_QUOTE=4, SEMI_COLON=5, LESS_THAN=6, 
		GREATER_THAN=7, BACKQUOTE=8, NEWLINE=9, WHITESPACE=10;
	public static final int
		RULE_command = 0, RULE_pipe = 1, RULE_seq = 2, RULE_call = 3, RULE_atom = 4, 
		RULE_argument = 5, RULE_redirection = 6, RULE_quoted = 7, RULE_singleQuoted = 8, 
		RULE_doubleQuoted = 9, RULE_backQuoted = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "pipe", "seq", "call", "atom", "argument", "redirection", 
			"quoted", "singleQuoted", "doubleQuoted", "backQuoted"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'|'", "'''", "'\"'", "';'", "'<'", "'>'", "'`'", "'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "UNQUOTED", "PIPE", "SINGLE_QUOTE", "DOUBLE_QUOTE", "SEMI_COLON", 
			"LESS_THAN", "GREATER_THAN", "BACKQUOTE", "NEWLINE", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ShellGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ShellGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public SeqContext seq() {
			return getRuleContext(SeqContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_command);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(22);
				pipe();
				}
				break;
			case 2:
				{
				setState(23);
				seq();
				}
				break;
			case 3:
				{
				setState(24);
				call();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipeContext extends ParserRuleContext {
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public TerminalNode PIPE() { return getToken(ShellGrammarParser.PIPE, 0); }
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public PipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipe; }
	}

	public final PipeContext pipe() throws RecognitionException {
		PipeContext _localctx = new PipeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_pipe);
		try {
			setState(35);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				call();
				setState(28);
				match(PIPE);
				setState(29);
				call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				call();
				setState(32);
				match(PIPE);
				setState(33);
				pipe();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SeqContext extends ParserRuleContext {
		public TerminalNode SEMI_COLON() { return getToken(ShellGrammarParser.SEMI_COLON, 0); }
		public List<PipeContext> pipe() {
			return getRuleContexts(PipeContext.class);
		}
		public PipeContext pipe(int i) {
			return getRuleContext(PipeContext.class,i);
		}
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public SeqContext seq() {
			return getRuleContext(SeqContext.class,0);
		}
		public SeqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seq; }
	}

	public final SeqContext seq() throws RecognitionException {
		SeqContext _localctx = new SeqContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_seq);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(37);
				pipe();
				}
				break;
			case 2:
				{
				setState(38);
				call();
				}
				break;
			}
			setState(41);
			match(SEMI_COLON);
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(42);
				pipe();
				}
				break;
			case 2:
				{
				setState(43);
				seq();
				}
				break;
			case 3:
				{
				setState(44);
				call();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallContext extends ParserRuleContext {
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(ShellGrammarParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(ShellGrammarParser.WHITESPACE, i);
		}
		public List<RedirectionContext> redirection() {
			return getRuleContexts(RedirectionContext.class);
		}
		public RedirectionContext redirection(int i) {
			return getRuleContext(RedirectionContext.class,i);
		}
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_call);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WHITESPACE) {
				{
				{
				setState(47);
				match(WHITESPACE);
				}
				}
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LESS_THAN || _la==GREATER_THAN) {
				{
				{
				setState(53);
				redirection();
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WHITESPACE) {
					{
					{
					setState(54);
					match(WHITESPACE);
					}
					}
					setState(59);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(65);
			argument();
			setState(75);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(69);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==WHITESPACE) {
						{
						{
						setState(66);
						match(WHITESPACE);
						}
						}
						setState(71);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(72);
					atom();
					}
					} 
				}
				setState(77);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WHITESPACE) {
				{
				{
				setState(78);
				match(WHITESPACE);
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public RedirectionContext redirection() {
			return getRuleContext(RedirectionContext.class,0);
		}
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_atom);
		try {
			setState(86);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LESS_THAN:
			case GREATER_THAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				redirection();
				}
				break;
			case UNQUOTED:
			case SINGLE_QUOTE:
			case DOUBLE_QUOTE:
			case BACKQUOTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				argument();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentContext extends ParserRuleContext {
		public List<QuotedContext> quoted() {
			return getRuleContexts(QuotedContext.class);
		}
		public QuotedContext quoted(int i) {
			return getRuleContext(QuotedContext.class,i);
		}
		public List<TerminalNode> UNQUOTED() { return getTokens(ShellGrammarParser.UNQUOTED); }
		public TerminalNode UNQUOTED(int i) {
			return getToken(ShellGrammarParser.UNQUOTED, i);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_argument);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(90); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(90);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case SINGLE_QUOTE:
					case DOUBLE_QUOTE:
					case BACKQUOTE:
						{
						setState(88);
						quoted();
						}
						break;
					case UNQUOTED:
						{
						setState(89);
						match(UNQUOTED);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(92); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RedirectionContext extends ParserRuleContext {
		public TerminalNode LESS_THAN() { return getToken(ShellGrammarParser.LESS_THAN, 0); }
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(ShellGrammarParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(ShellGrammarParser.WHITESPACE, i);
		}
		public TerminalNode GREATER_THAN() { return getToken(ShellGrammarParser.GREATER_THAN, 0); }
		public RedirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_redirection; }
	}

	public final RedirectionContext redirection() throws RecognitionException {
		RedirectionContext _localctx = new RedirectionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_redirection);
		int _la;
		try {
			setState(110);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LESS_THAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(LESS_THAN);
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WHITESPACE) {
					{
					{
					setState(95);
					match(WHITESPACE);
					}
					}
					setState(100);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(101);
				argument();
				}
				break;
			case GREATER_THAN:
				enterOuterAlt(_localctx, 2);
				{
				setState(102);
				match(GREATER_THAN);
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WHITESPACE) {
					{
					{
					setState(103);
					match(WHITESPACE);
					}
					}
					setState(108);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(109);
				argument();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QuotedContext extends ParserRuleContext {
		public SingleQuotedContext singleQuoted() {
			return getRuleContext(SingleQuotedContext.class,0);
		}
		public DoubleQuotedContext doubleQuoted() {
			return getRuleContext(DoubleQuotedContext.class,0);
		}
		public BackQuotedContext backQuoted() {
			return getRuleContext(BackQuotedContext.class,0);
		}
		public QuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quoted; }
	}

	public final QuotedContext quoted() throws RecognitionException {
		QuotedContext _localctx = new QuotedContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_quoted);
		try {
			setState(115);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINGLE_QUOTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				singleQuoted();
				}
				break;
			case DOUBLE_QUOTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(113);
				doubleQuoted();
				}
				break;
			case BACKQUOTE:
				enterOuterAlt(_localctx, 3);
				{
				setState(114);
				backQuoted();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SingleQuotedContext extends ParserRuleContext {
		public List<TerminalNode> SINGLE_QUOTE() { return getTokens(ShellGrammarParser.SINGLE_QUOTE); }
		public TerminalNode SINGLE_QUOTE(int i) {
			return getToken(ShellGrammarParser.SINGLE_QUOTE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ShellGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ShellGrammarParser.NEWLINE, i);
		}
		public SingleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleQuoted; }
	}

	public final SingleQuotedContext singleQuoted() throws RecognitionException {
		SingleQuotedContext _localctx = new SingleQuotedContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_singleQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(SINGLE_QUOTE);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1526L) != 0)) {
				{
				{
				setState(118);
				_la = _input.LA(1);
				if ( _la <= 0 || (_la==SINGLE_QUOTE || _la==NEWLINE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(124);
			match(SINGLE_QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoubleQuotedContext extends ParserRuleContext {
		public List<TerminalNode> DOUBLE_QUOTE() { return getTokens(ShellGrammarParser.DOUBLE_QUOTE); }
		public TerminalNode DOUBLE_QUOTE(int i) {
			return getToken(ShellGrammarParser.DOUBLE_QUOTE, i);
		}
		public List<BackQuotedContext> backQuoted() {
			return getRuleContexts(BackQuotedContext.class);
		}
		public BackQuotedContext backQuoted(int i) {
			return getRuleContext(BackQuotedContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ShellGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ShellGrammarParser.NEWLINE, i);
		}
		public List<TerminalNode> BACKQUOTE() { return getTokens(ShellGrammarParser.BACKQUOTE); }
		public TerminalNode BACKQUOTE(int i) {
			return getToken(ShellGrammarParser.BACKQUOTE, i);
		}
		public DoubleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doubleQuoted; }
	}

	public final DoubleQuotedContext doubleQuoted() throws RecognitionException {
		DoubleQuotedContext _localctx = new DoubleQuotedContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_doubleQuoted);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(DOUBLE_QUOTE);
			setState(131);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(129);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case BACKQUOTE:
						{
						setState(127);
						backQuoted();
						}
						break;
					case UNQUOTED:
					case PIPE:
					case SINGLE_QUOTE:
					case DOUBLE_QUOTE:
					case SEMI_COLON:
					case LESS_THAN:
					case GREATER_THAN:
					case WHITESPACE:
						{
						setState(128);
						_la = _input.LA(1);
						if ( _la <= 0 || (_la==BACKQUOTE || _la==NEWLINE) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(133);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			setState(134);
			match(DOUBLE_QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BackQuotedContext extends ParserRuleContext {
		public List<TerminalNode> BACKQUOTE() { return getTokens(ShellGrammarParser.BACKQUOTE); }
		public TerminalNode BACKQUOTE(int i) {
			return getToken(ShellGrammarParser.BACKQUOTE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ShellGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ShellGrammarParser.NEWLINE, i);
		}
		public BackQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_backQuoted; }
	}

	public final BackQuotedContext backQuoted() throws RecognitionException {
		BackQuotedContext _localctx = new BackQuotedContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_backQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(BACKQUOTE);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1278L) != 0)) {
				{
				{
				setState(137);
				_la = _input.LA(1);
				if ( _la <= 0 || (_la==BACKQUOTE || _la==NEWLINE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(143);
			match(BACKQUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\n\u0092\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0003\u0000\u001a\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001$\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0003\u0002(\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002.\b\u0002\u0001\u0003\u0005"+
		"\u00031\b\u0003\n\u0003\f\u00034\t\u0003\u0001\u0003\u0001\u0003\u0005"+
		"\u00038\b\u0003\n\u0003\f\u0003;\t\u0003\u0005\u0003=\b\u0003\n\u0003"+
		"\f\u0003@\t\u0003\u0001\u0003\u0001\u0003\u0005\u0003D\b\u0003\n\u0003"+
		"\f\u0003G\t\u0003\u0001\u0003\u0005\u0003J\b\u0003\n\u0003\f\u0003M\t"+
		"\u0003\u0001\u0003\u0005\u0003P\b\u0003\n\u0003\f\u0003S\t\u0003\u0001"+
		"\u0004\u0001\u0004\u0003\u0004W\b\u0004\u0001\u0005\u0001\u0005\u0004"+
		"\u0005[\b\u0005\u000b\u0005\f\u0005\\\u0001\u0006\u0001\u0006\u0005\u0006"+
		"a\b\u0006\n\u0006\f\u0006d\t\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0005\u0006i\b\u0006\n\u0006\f\u0006l\t\u0006\u0001\u0006\u0003\u0006"+
		"o\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007t\b\u0007\u0001"+
		"\b\u0001\b\u0005\bx\b\b\n\b\f\b{\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0005\t\u0082\b\t\n\t\f\t\u0085\t\t\u0001\t\u0001\t\u0001\n\u0001\n"+
		"\u0005\n\u008b\b\n\n\n\f\n\u008e\t\n\u0001\n\u0001\n\u0001\n\u0000\u0000"+
		"\u000b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0000\u0002"+
		"\u0002\u0000\u0003\u0003\t\t\u0001\u0000\b\t\u00a0\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0002#\u0001\u0000\u0000\u0000\u0004\'\u0001\u0000\u0000"+
		"\u0000\u00062\u0001\u0000\u0000\u0000\bV\u0001\u0000\u0000\u0000\nZ\u0001"+
		"\u0000\u0000\u0000\fn\u0001\u0000\u0000\u0000\u000es\u0001\u0000\u0000"+
		"\u0000\u0010u\u0001\u0000\u0000\u0000\u0012~\u0001\u0000\u0000\u0000\u0014"+
		"\u0088\u0001\u0000\u0000\u0000\u0016\u001a\u0003\u0002\u0001\u0000\u0017"+
		"\u001a\u0003\u0004\u0002\u0000\u0018\u001a\u0003\u0006\u0003\u0000\u0019"+
		"\u0016\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u0019"+
		"\u0018\u0001\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a"+
		"\u0001\u0001\u0000\u0000\u0000\u001b\u001c\u0003\u0006\u0003\u0000\u001c"+
		"\u001d\u0005\u0002\u0000\u0000\u001d\u001e\u0003\u0006\u0003\u0000\u001e"+
		"$\u0001\u0000\u0000\u0000\u001f \u0003\u0006\u0003\u0000 !\u0005\u0002"+
		"\u0000\u0000!\"\u0003\u0002\u0001\u0000\"$\u0001\u0000\u0000\u0000#\u001b"+
		"\u0001\u0000\u0000\u0000#\u001f\u0001\u0000\u0000\u0000$\u0003\u0001\u0000"+
		"\u0000\u0000%(\u0003\u0002\u0001\u0000&(\u0003\u0006\u0003\u0000\'%\u0001"+
		"\u0000\u0000\u0000\'&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000\u0000"+
		")-\u0005\u0005\u0000\u0000*.\u0003\u0002\u0001\u0000+.\u0003\u0004\u0002"+
		"\u0000,.\u0003\u0006\u0003\u0000-*\u0001\u0000\u0000\u0000-+\u0001\u0000"+
		"\u0000\u0000-,\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000.\u0005"+
		"\u0001\u0000\u0000\u0000/1\u0005\n\u0000\u00000/\u0001\u0000\u0000\u0000"+
		"14\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u000023\u0001\u0000\u0000"+
		"\u00003>\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u000059\u0003\f\u0006"+
		"\u000068\u0005\n\u0000\u000076\u0001\u0000\u0000\u00008;\u0001\u0000\u0000"+
		"\u000097\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:=\u0001\u0000"+
		"\u0000\u0000;9\u0001\u0000\u0000\u0000<5\u0001\u0000\u0000\u0000=@\u0001"+
		"\u0000\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000"+
		"?A\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000AK\u0003\n\u0005\u0000"+
		"BD\u0005\n\u0000\u0000CB\u0001\u0000\u0000\u0000DG\u0001\u0000\u0000\u0000"+
		"EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001\u0000\u0000"+
		"\u0000GE\u0001\u0000\u0000\u0000HJ\u0003\b\u0004\u0000IE\u0001\u0000\u0000"+
		"\u0000JM\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000"+
		"\u0000\u0000LQ\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000NP\u0005"+
		"\n\u0000\u0000ON\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001"+
		"\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000R\u0007\u0001\u0000\u0000"+
		"\u0000SQ\u0001\u0000\u0000\u0000TW\u0003\f\u0006\u0000UW\u0003\n\u0005"+
		"\u0000VT\u0001\u0000\u0000\u0000VU\u0001\u0000\u0000\u0000W\t\u0001\u0000"+
		"\u0000\u0000X[\u0003\u000e\u0007\u0000Y[\u0005\u0001\u0000\u0000ZX\u0001"+
		"\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000"+
		"\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u000b\u0001\u0000"+
		"\u0000\u0000^b\u0005\u0006\u0000\u0000_a\u0005\n\u0000\u0000`_\u0001\u0000"+
		"\u0000\u0000ad\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000bc\u0001"+
		"\u0000\u0000\u0000ce\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000"+
		"eo\u0003\n\u0005\u0000fj\u0005\u0007\u0000\u0000gi\u0005\n\u0000\u0000"+
		"hg\u0001\u0000\u0000\u0000il\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000"+
		"\u0000jk\u0001\u0000\u0000\u0000km\u0001\u0000\u0000\u0000lj\u0001\u0000"+
		"\u0000\u0000mo\u0003\n\u0005\u0000n^\u0001\u0000\u0000\u0000nf\u0001\u0000"+
		"\u0000\u0000o\r\u0001\u0000\u0000\u0000pt\u0003\u0010\b\u0000qt\u0003"+
		"\u0012\t\u0000rt\u0003\u0014\n\u0000sp\u0001\u0000\u0000\u0000sq\u0001"+
		"\u0000\u0000\u0000sr\u0001\u0000\u0000\u0000t\u000f\u0001\u0000\u0000"+
		"\u0000uy\u0005\u0003\u0000\u0000vx\b\u0000\u0000\u0000wv\u0001\u0000\u0000"+
		"\u0000x{\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001\u0000"+
		"\u0000\u0000z|\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000|}\u0005"+
		"\u0003\u0000\u0000}\u0011\u0001\u0000\u0000\u0000~\u0083\u0005\u0004\u0000"+
		"\u0000\u007f\u0082\u0003\u0014\n\u0000\u0080\u0082\b\u0001\u0000\u0000"+
		"\u0081\u007f\u0001\u0000\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000"+
		"\u0082\u0085\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0086\u0001\u0000\u0000\u0000"+
		"\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u0087\u0005\u0004\u0000\u0000"+
		"\u0087\u0013\u0001\u0000\u0000\u0000\u0088\u008c\u0005\b\u0000\u0000\u0089"+
		"\u008b\b\u0001\u0000\u0000\u008a\u0089\u0001\u0000\u0000\u0000\u008b\u008e"+
		"\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008c\u008d"+
		"\u0001\u0000\u0000\u0000\u008d\u008f\u0001\u0000\u0000\u0000\u008e\u008c"+
		"\u0001\u0000\u0000\u0000\u008f\u0090\u0005\b\u0000\u0000\u0090\u0015\u0001"+
		"\u0000\u0000\u0000\u0015\u0019#\'-29>EKQVZ\\bjnsy\u0081\u0083\u008c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}