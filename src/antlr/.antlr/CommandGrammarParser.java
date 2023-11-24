// Generated from /home/ayush/comp0010-shell-python-p22/src/antlr/CommandGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CommandGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PIPE=1, SINGLE_QUOTE=2, DOUBLE_QUOTE=3, SEMI_COLON=4, LESS_THAN=5, GREATER_THAN=6, 
		BACKQUOTE=7, NEWLINE=8, WHITESPACE=9, NON_KEYWORD=10, UNQUOTED=11;
	public static final int
		RULE_command = 0, RULE_pipe = 1, RULE_seq = 2, RULE_call = 3, RULE_quoted = 4, 
		RULE_singleQuoted = 5, RULE_backQuoted = 6, RULE_doubleQuoted = 7, RULE_atom = 8, 
		RULE_argument = 9, RULE_redirection = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "pipe", "seq", "call", "quoted", "singleQuoted", "backQuoted", 
			"doubleQuoted", "atom", "argument", "redirection"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'|'", "'''", "'\"'", "';'", "'<'", "'>'", "'`'", "'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PIPE", "SINGLE_QUOTE", "DOUBLE_QUOTE", "SEMI_COLON", "LESS_THAN", 
			"GREATER_THAN", "BACKQUOTE", "NEWLINE", "WHITESPACE", "NON_KEYWORD", 
			"UNQUOTED"
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
	public String getGrammarFileName() { return "CommandGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CommandGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CommandGrammarParser.EOF, 0); }
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
			setState(27);
			match(EOF);
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
		public TerminalNode PIPE() { return getToken(CommandGrammarParser.PIPE, 0); }
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
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(29);
				call();
				setState(30);
				match(PIPE);
				setState(31);
				call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				call();
				setState(34);
				match(PIPE);
				setState(35);
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
		public TerminalNode SEMI_COLON() { return getToken(CommandGrammarParser.SEMI_COLON, 0); }
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
			setState(41);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(39);
				pipe();
				}
				break;
			case 2:
				{
				setState(40);
				call();
				}
				break;
			}
			setState(43);
			match(SEMI_COLON);
			setState(47);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(44);
				pipe();
				}
				break;
			case 2:
				{
				setState(45);
				seq();
				}
				break;
			case 3:
				{
				setState(46);
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
		public List<TerminalNode> WHITESPACE() { return getTokens(CommandGrammarParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(CommandGrammarParser.WHITESPACE, i);
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
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WHITESPACE) {
				{
				{
				setState(49);
				match(WHITESPACE);
				}
				}
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LESS_THAN || _la==GREATER_THAN) {
				{
				{
				setState(55);
				redirection();
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WHITESPACE) {
					{
					{
					setState(56);
					match(WHITESPACE);
					}
					}
					setState(61);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(67);
			argument();
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(71);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==WHITESPACE) {
						{
						{
						setState(68);
						match(WHITESPACE);
						}
						}
						setState(73);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(74);
					atom();
					}
					} 
				}
				setState(79);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WHITESPACE) {
				{
				{
				setState(80);
				match(WHITESPACE);
				}
				}
				setState(85);
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
		enterRule(_localctx, 8, RULE_quoted);
		try {
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINGLE_QUOTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(86);
				singleQuoted();
				}
				break;
			case DOUBLE_QUOTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				doubleQuoted();
				}
				break;
			case BACKQUOTE:
				enterOuterAlt(_localctx, 3);
				{
				setState(88);
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
		public List<TerminalNode> SINGLE_QUOTE() { return getTokens(CommandGrammarParser.SINGLE_QUOTE); }
		public TerminalNode SINGLE_QUOTE(int i) {
			return getToken(CommandGrammarParser.SINGLE_QUOTE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CommandGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CommandGrammarParser.NEWLINE, i);
		}
		public SingleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleQuoted; }
	}

	public final SingleQuotedContext singleQuoted() throws RecognitionException {
		SingleQuotedContext _localctx = new SingleQuotedContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_singleQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(SINGLE_QUOTE);
			setState(93); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(92);
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
				setState(95); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3834L) != 0) );
			setState(97);
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
	public static class BackQuotedContext extends ParserRuleContext {
		public List<TerminalNode> BACKQUOTE() { return getTokens(CommandGrammarParser.BACKQUOTE); }
		public TerminalNode BACKQUOTE(int i) {
			return getToken(CommandGrammarParser.BACKQUOTE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CommandGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CommandGrammarParser.NEWLINE, i);
		}
		public BackQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_backQuoted; }
	}

	public final BackQuotedContext backQuoted() throws RecognitionException {
		BackQuotedContext _localctx = new BackQuotedContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_backQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(BACKQUOTE);
			setState(101); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(100);
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
				setState(103); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3710L) != 0) );
			setState(105);
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

	@SuppressWarnings("CheckReturnValue")
	public static class DoubleQuotedContext extends ParserRuleContext {
		public List<TerminalNode> DOUBLE_QUOTE() { return getTokens(CommandGrammarParser.DOUBLE_QUOTE); }
		public TerminalNode DOUBLE_QUOTE(int i) {
			return getToken(CommandGrammarParser.DOUBLE_QUOTE, i);
		}
		public List<BackQuotedContext> backQuoted() {
			return getRuleContexts(BackQuotedContext.class);
		}
		public BackQuotedContext backQuoted(int i) {
			return getRuleContext(BackQuotedContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CommandGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CommandGrammarParser.NEWLINE, i);
		}
		public List<TerminalNode> BACKQUOTE() { return getTokens(CommandGrammarParser.BACKQUOTE); }
		public TerminalNode BACKQUOTE(int i) {
			return getToken(CommandGrammarParser.BACKQUOTE, i);
		}
		public DoubleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doubleQuoted; }
	}

	public final DoubleQuotedContext doubleQuoted() throws RecognitionException {
		DoubleQuotedContext _localctx = new DoubleQuotedContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_doubleQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(DOUBLE_QUOTE);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3830L) != 0)) {
				{
				setState(110);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BACKQUOTE:
					{
					setState(108);
					backQuoted();
					}
					break;
				case PIPE:
				case SINGLE_QUOTE:
				case SEMI_COLON:
				case LESS_THAN:
				case GREATER_THAN:
				case WHITESPACE:
				case NON_KEYWORD:
				case UNQUOTED:
					{
					setState(109);
					_la = _input.LA(1);
					if ( _la <= 0 || ((((_la) & ~0x3f) == 0 && ((1L << _la) & 392L) != 0)) ) {
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
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(115);
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
		enterRule(_localctx, 16, RULE_atom);
		try {
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LESS_THAN:
			case GREATER_THAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(117);
				redirection();
				}
				break;
			case SINGLE_QUOTE:
			case DOUBLE_QUOTE:
			case BACKQUOTE:
			case UNQUOTED:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
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
		public List<TerminalNode> UNQUOTED() { return getTokens(CommandGrammarParser.UNQUOTED); }
		public TerminalNode UNQUOTED(int i) {
			return getToken(CommandGrammarParser.UNQUOTED, i);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_argument);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(123); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(123);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case SINGLE_QUOTE:
					case DOUBLE_QUOTE:
					case BACKQUOTE:
						{
						setState(121);
						quoted();
						}
						break;
					case UNQUOTED:
						{
						setState(122);
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
				setState(125); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
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
		public TerminalNode LESS_THAN() { return getToken(CommandGrammarParser.LESS_THAN, 0); }
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(CommandGrammarParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(CommandGrammarParser.WHITESPACE, i);
		}
		public TerminalNode GREATER_THAN() { return getToken(CommandGrammarParser.GREATER_THAN, 0); }
		public RedirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_redirection; }
	}

	public final RedirectionContext redirection() throws RecognitionException {
		RedirectionContext _localctx = new RedirectionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_redirection);
		int _la;
		try {
			setState(143);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LESS_THAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				match(LESS_THAN);
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WHITESPACE) {
					{
					{
					setState(128);
					match(WHITESPACE);
					}
					}
					setState(133);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(134);
				argument();
				}
				break;
			case GREATER_THAN:
				enterOuterAlt(_localctx, 2);
				{
				setState(135);
				match(GREATER_THAN);
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WHITESPACE) {
					{
					{
					setState(136);
					match(WHITESPACE);
					}
					}
					setState(141);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(142);
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

	public static final String _serializedATN =
		"\u0004\u0001\u000b\u0092\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0003\u0000\u001a\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001&\b\u0001\u0001\u0002\u0001\u0002\u0003\u0002"+
		"*\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"0\b\u0002\u0001\u0003\u0005\u00033\b\u0003\n\u0003\f\u00036\t\u0003\u0001"+
		"\u0003\u0001\u0003\u0005\u0003:\b\u0003\n\u0003\f\u0003=\t\u0003\u0005"+
		"\u0003?\b\u0003\n\u0003\f\u0003B\t\u0003\u0001\u0003\u0001\u0003\u0005"+
		"\u0003F\b\u0003\n\u0003\f\u0003I\t\u0003\u0001\u0003\u0005\u0003L\b\u0003"+
		"\n\u0003\f\u0003O\t\u0003\u0001\u0003\u0005\u0003R\b\u0003\n\u0003\f\u0003"+
		"U\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004Z\b\u0004\u0001"+
		"\u0005\u0001\u0005\u0004\u0005^\b\u0005\u000b\u0005\f\u0005_\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0004\u0006f\b\u0006\u000b\u0006"+
		"\f\u0006g\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0005\u0007o\b\u0007\n\u0007\f\u0007r\t\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0003\bx\b\b\u0001\t\u0001\t\u0004\t|\b\t\u000b\t\f\t"+
		"}\u0001\n\u0001\n\u0005\n\u0082\b\n\n\n\f\n\u0085\t\n\u0001\n\u0001\n"+
		"\u0001\n\u0005\n\u008a\b\n\n\n\f\n\u008d\t\n\u0001\n\u0003\n\u0090\b\n"+
		"\u0001\n\u0000\u0000\u000b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0000\u0003\u0002\u0000\u0002\u0002\b\b\u0001\u0000\u0007\b\u0002"+
		"\u0000\u0003\u0003\u0007\b\u00a0\u0000\u0019\u0001\u0000\u0000\u0000\u0002"+
		"%\u0001\u0000\u0000\u0000\u0004)\u0001\u0000\u0000\u0000\u00064\u0001"+
		"\u0000\u0000\u0000\bY\u0001\u0000\u0000\u0000\n[\u0001\u0000\u0000\u0000"+
		"\fc\u0001\u0000\u0000\u0000\u000ek\u0001\u0000\u0000\u0000\u0010w\u0001"+
		"\u0000\u0000\u0000\u0012{\u0001\u0000\u0000\u0000\u0014\u008f\u0001\u0000"+
		"\u0000\u0000\u0016\u001a\u0003\u0002\u0001\u0000\u0017\u001a\u0003\u0004"+
		"\u0002\u0000\u0018\u001a\u0003\u0006\u0003\u0000\u0019\u0016\u0001\u0000"+
		"\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u0019\u0018\u0001\u0000"+
		"\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u001b\u0001\u0000"+
		"\u0000\u0000\u001b\u001c\u0005\u0000\u0000\u0001\u001c\u0001\u0001\u0000"+
		"\u0000\u0000\u001d\u001e\u0003\u0006\u0003\u0000\u001e\u001f\u0005\u0001"+
		"\u0000\u0000\u001f \u0003\u0006\u0003\u0000 &\u0001\u0000\u0000\u0000"+
		"!\"\u0003\u0006\u0003\u0000\"#\u0005\u0001\u0000\u0000#$\u0003\u0002\u0001"+
		"\u0000$&\u0001\u0000\u0000\u0000%\u001d\u0001\u0000\u0000\u0000%!\u0001"+
		"\u0000\u0000\u0000&\u0003\u0001\u0000\u0000\u0000\'*\u0003\u0002\u0001"+
		"\u0000(*\u0003\u0006\u0003\u0000)\'\u0001\u0000\u0000\u0000)(\u0001\u0000"+
		"\u0000\u0000*+\u0001\u0000\u0000\u0000+/\u0005\u0004\u0000\u0000,0\u0003"+
		"\u0002\u0001\u0000-0\u0003\u0004\u0002\u0000.0\u0003\u0006\u0003\u0000"+
		"/,\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000/.\u0001\u0000\u0000"+
		"\u0000/0\u0001\u0000\u0000\u00000\u0005\u0001\u0000\u0000\u000013\u0005"+
		"\t\u0000\u000021\u0001\u0000\u0000\u000036\u0001\u0000\u0000\u000042\u0001"+
		"\u0000\u0000\u000045\u0001\u0000\u0000\u00005@\u0001\u0000\u0000\u0000"+
		"64\u0001\u0000\u0000\u00007;\u0003\u0014\n\u00008:\u0005\t\u0000\u0000"+
		"98\u0001\u0000\u0000\u0000:=\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000"+
		"\u0000;<\u0001\u0000\u0000\u0000<?\u0001\u0000\u0000\u0000=;\u0001\u0000"+
		"\u0000\u0000>7\u0001\u0000\u0000\u0000?B\u0001\u0000\u0000\u0000@>\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AC\u0001\u0000\u0000\u0000"+
		"B@\u0001\u0000\u0000\u0000CM\u0003\u0012\t\u0000DF\u0005\t\u0000\u0000"+
		"ED\u0001\u0000\u0000\u0000FI\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000"+
		"\u0000GH\u0001\u0000\u0000\u0000HJ\u0001\u0000\u0000\u0000IG\u0001\u0000"+
		"\u0000\u0000JL\u0003\u0010\b\u0000KG\u0001\u0000\u0000\u0000LO\u0001\u0000"+
		"\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NS\u0001"+
		"\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PR\u0005\t\u0000\u0000QP\u0001"+
		"\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000"+
		"ST\u0001\u0000\u0000\u0000T\u0007\u0001\u0000\u0000\u0000US\u0001\u0000"+
		"\u0000\u0000VZ\u0003\n\u0005\u0000WZ\u0003\u000e\u0007\u0000XZ\u0003\f"+
		"\u0006\u0000YV\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YX\u0001"+
		"\u0000\u0000\u0000Z\t\u0001\u0000\u0000\u0000[]\u0005\u0002\u0000\u0000"+
		"\\^\b\u0000\u0000\u0000]\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000"+
		"\u0000_]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`a\u0001\u0000"+
		"\u0000\u0000ab\u0005\u0002\u0000\u0000b\u000b\u0001\u0000\u0000\u0000"+
		"ce\u0005\u0007\u0000\u0000df\b\u0001\u0000\u0000ed\u0001\u0000\u0000\u0000"+
		"fg\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000"+
		"\u0000hi\u0001\u0000\u0000\u0000ij\u0005\u0007\u0000\u0000j\r\u0001\u0000"+
		"\u0000\u0000kp\u0005\u0003\u0000\u0000lo\u0003\f\u0006\u0000mo\b\u0002"+
		"\u0000\u0000nl\u0001\u0000\u0000\u0000nm\u0001\u0000\u0000\u0000or\u0001"+
		"\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000"+
		"qs\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000st\u0005\u0003\u0000"+
		"\u0000t\u000f\u0001\u0000\u0000\u0000ux\u0003\u0014\n\u0000vx\u0003\u0012"+
		"\t\u0000wu\u0001\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000x\u0011\u0001"+
		"\u0000\u0000\u0000y|\u0003\b\u0004\u0000z|\u0005\u000b\u0000\u0000{y\u0001"+
		"\u0000\u0000\u0000{z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000"+
		"}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0013\u0001\u0000"+
		"\u0000\u0000\u007f\u0083\u0005\u0005\u0000\u0000\u0080\u0082\u0005\t\u0000"+
		"\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000"+
		"\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000"+
		"\u0000\u0084\u0086\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000"+
		"\u0000\u0086\u0090\u0003\u0012\t\u0000\u0087\u008b\u0005\u0006\u0000\u0000"+
		"\u0088\u008a\u0005\t\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a"+
		"\u008d\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b"+
		"\u008c\u0001\u0000\u0000\u0000\u008c\u008e\u0001\u0000\u0000\u0000\u008d"+
		"\u008b\u0001\u0000\u0000\u0000\u008e\u0090\u0003\u0012\t\u0000\u008f\u007f"+
		"\u0001\u0000\u0000\u0000\u008f\u0087\u0001\u0000\u0000\u0000\u0090\u0015"+
		"\u0001\u0000\u0000\u0000\u0015\u0019%)/4;@GMSY_gnpw{}\u0083\u008b\u008f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}