default(parisize, 256000000);

fibre_h(q, r, m0) =
{
  my(B, C, u, h);
  B = prod(k = 0, r - 1, x - Mod(k, q));
  C = prod(aa = r, q - 1, x - Mod(aa, q));
  u = C * deriv(B);
  h = u - Mod(m0, q);
  return(h);
}

fibre_L_pari(q, r, m0) =
{
  my(h, F, nr, L, i, f, d, a, g, o);
  h = fibre_h(q, r, m0);
  F = factormod(h, q);
  nr = matsize(F)[1];
  L = 1;
  for(i = 1, nr,
    f = F[i, 1];
    d = poldegree(f);
    if(d >= 2,
      a = ffgen(f);
      g = a^q - a;
      if(g != 0,
        o = fforder(g);
        print(Str("  factor d=", d, " fforder=", o));
        L = lcm(L, o)
      ,
        print(Str("  factor d=", d, " wp=0"))
      )
    ,
      print(Str("  factor d=", d, " linear"))
    )
  );
  return(L);
}

{
  my(pairs, i, q, r, m0, L);
  pairs = [[11,2,6],[11,2,7],[11,2,8],[11,2,9],[11,3,6],[5,1,0],[5,1,1],[5,1,2],[5,1,3],[7,1,0],[7,1,1],[7,1,2],[11,1,1],[11,1,2],[13,1,1]];
  for(i = 1, #pairs,
    q = pairs[i][1];
    r = pairs[i][2];
    m0 = pairs[i][3];
    print(Str("BEGIN ", q, " ", r, " ", m0));
    L = fibre_L_pari(q, r, m0);
    print(Str("PARI ", q, " ", r, " ", m0, " L=", L))
  );
  print("PARI_DONE");
}
quit;
