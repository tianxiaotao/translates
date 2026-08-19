var r = null;
var window = {}
window.gtk = '320305.131321201';

function e(t, e) {
	(null == e || e > t.length) && (e = t.length);
	for (var n = 0, r = new Array(e); n < e; n++)
		r[n] = t[n];
	return r
}

function n(t, e) {
	for (var n = 0; n < e.length - 2; n += 3) {
		var r = e.charAt(n + 2);
		r = "a" <= r ? r.charCodeAt(0) - 87 : Number(r),
		r = "+" === e.charAt(n + 1) ? t >>> r : t << r,
		t = "+" === e.charAt(n) ? t + r & 4294967295 : t ^ r
	}
	return t
}

function a( t ){

	var o, i = t.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
	if (null === i) {
		var a = t.length;
		a > 30 && (t = "".concat(t.substr(0, 10)).concat(t.substr(Math.floor(a / 2) - 5, 10)).concat(t.substr(-10, 10)))
	} else {
		for (var s = t.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), c = 0, u = s.length, l = []; c < u; c++)
			"" !== s[c] && l.push.apply(l, function(t) {
				if (Array.isArray(t))
					return e(t)
			}(o = s[c].split("")) || function(t) {
				if ("undefined" != typeof Symbol && null != t[Symbol.iterator] || null != t["@@iterator"])
					return Array.from(t)
			}(o) || function(t, n) {
				if (t) {
					if ("string" == typeof t)
						return e(t, n);
					var r = Object.prototype.toString.call(t).slice(8, -1);
					return "Object" === r && t.constructor && (r = t.constructor.name),
					"Map" === r || "Set" === r ? Array.from(t) : "Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? e(t, n) : void 0
				}
			}(o) || function() {
				throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
			}()),
			c !== u - 1 && l.push(i[c]);
		var p = l.length;
		p > 30 && (t = l.slice(0, 10).join("") + l.slice(Math.floor(p / 2) - 5, Math.floor(p / 2) + 5).join("") + l.slice(-10).join(""))
	}

	for (var d = "".concat(String.fromCharCode(103)).concat(String.fromCharCode(116)).concat(String.fromCharCode(107)), h = (null !== r ? r : (r = window[d] || "") || "").split("."), f = Number(h[0]) || 0, m = Number(h[1]) || 0, g = [], y = 0, v = 0; v < t.length; v++) {
		var _ = t.charCodeAt(v);
		_ < 128 ? g[y++] = _ : (_ < 2048 ? g[y++] = _ >> 6 | 192 : (55296 == (64512 & _) && v + 1 < t.length && 56320 == (64512 & t.charCodeAt(v + 1)) ? (_ = 65536 + ((1023 & _) << 10) + (1023 & t.charCodeAt(++v)),
		g[y++] = _ >> 18 | 240,
		g[y++] = _ >> 12 & 63 | 128) : g[y++] = _ >> 12 | 224,
		g[y++] = _ >> 6 & 63 | 128),
		g[y++] = 63 & _ | 128)
	}

	for (var b = f, w = "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(97)) + "".concat(String.fromCharCode(94)).concat(String.fromCharCode(43)).concat(String.fromCharCode(54)), k = "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(51)) + "".concat(String.fromCharCode(94)).concat(String.fromCharCode(43)).concat(String.fromCharCode(98)) + "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(102)), x = 0; x < g.length; x++)
	{
		b = n(b += g[x], w);
	}

	return b = n(b, k),
	(b ^= m) < 0 && (b = 2147483648 + (2147483647 & b)),
	"".concat((b %= 1e6).toString(), ".").concat(b ^ f)
}


function get_trans_sign(r) {

	var t = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
	if (null === t) {
		var a = r.length;
		a > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(a / 2) - 5, 10) + r.substr(-10, 10))
	} else {
		for (var C = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), h = 0, f = C.length, u = []; f > h; h++)
			"" !== C[h] && u.push.apply(u, e(C[h].split(""))),
			h !== f - 1 && u.push(t[h]);
		var g = u.length;
		g > 30 && (r = u.slice(0, 10).join("") + u.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + u.slice(-10).join(""))
	}
	var l = void 0
	  , d = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
	l = window.gtk;
	for (var m = l.split("."), S = Number(m[0]) || 0, s = Number(m[1]) || 0, c = [], v = 0, F = 0; F < r.length; F++) {
		var p = r.charCodeAt(F);
		128 > p ? c[v++] = p : (2048 > p ? c[v++] = p >> 6 | 192 : (55296 === (64512 & p) && F + 1 < r.length && 56320 === (64512 & r.charCodeAt(F + 1)) ? (p = 65536 + ((1023 & p) << 10) + (1023 & r.charCodeAt(++F)),
		c[v++] = p >> 18 | 240,
		c[v++] = p >> 12 & 63 | 128) : c[v++] = p >> 12 | 224,
		c[v++] = p >> 6 & 63 | 128),
		c[v++] = 63 & p | 128)
	}
	for (var w = S, A = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), b = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), D = 0; D < c.length; D++)
		w += c[D],
		w = n(w, A);
	return w = n(w, b),
	w ^= s,
	0 > w && (w = (2147483647 & w) + 2147483648),
	w %= 1e6,
	w.toString() + "." + (w ^ S)
}

console.log( get_trans_sign( 'xxx' ) )