/*
  By Hironobu SUZUKI (C) 2006, hironobu -at- h2np -dot- net
  Copyright: GPL v2 or later.
  $Id: mt-bbp.c,v 1.6 2006/09/21 05:31:41 hironobu Exp hironobu $
 */
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <gmp.h>

#define VERBOSE  1

#define LOG_TEN_TWO  3.32192809488736234789
#define bprec(n) (int)(((n+10)*LOG_TEN_TWO)+2)

/* number of processor  */
#define PNUM  16
int pnum=1;

/* pi decimal precision */
#define DPREC 15000L

mpf_t A[PNUM], B[PNUM], C[PNUM], O[PNUM], fta[PNUM], ftb[PNUM], ftc[PNUM];
long int prec, dprec;
int loopdiv;

void *thread_func(void *v) {
  time_t t0, t1;
  int loopcounter=0;
  int i = (int)v;
  int j;
  int k;
  float percent;
  float fprec = (prec * 0.78) / ( LOG_TEN_TWO * pnum ) ;

  time(&t0);
  mpf_init(A[i]);
  mpf_init(B[i]);
  mpf_init(C[i]);
  mpf_init(O[i]);
  mpf_init(fta[i]);
  mpf_init(ftb[i]);
  mpf_init(ftc[i]);
  mpf_set_si(A[i],1) ;		        /*  A=1  */
  mpf_set_si(B[i],0) ;		        /*  B=0  */
  mpf_set_si(O[i],-1) ;		        /*  O=-1 */

  mpf_set_ui (fta[i], 16);              /* 16^n  (init)*/
  mpf_pow_ui(A[i], fta[i], i);	

  for ( j = i ; j < dprec; j+=pnum) {   /* but, j never be reached dprec */
    mpf_set_ui (fta[i], 8);	        /* 8  */
    mpf_mul_ui (B[i], fta[i], j);	/* 8n -> B */
    
    /* B is 8n */
    mpf_add_ui(fta[i],B[i],1);	        /*  8n + 1 -> B + 1 */
    mpf_ui_div(ftb[i],4,fta[i]);	/*  4/(8n+1) */

    mpf_add_ui(fta[i],B[i],4);	        /* 8n + 4 -> B + 4 */
    mpf_ui_div(ftc[i],2,fta[i]);	/* 2/(8n+4) */

    mpf_sub(fta[i], ftb[i], ftc[i]);	/* 4/(8n+1) -  2/(8n+4) */
      
    mpf_add_ui(ftb[i],B[i],5);	        /*  8n + 5 -> B + 5*/
    mpf_ui_div(ftc[i],1,ftb[i]);	/*  1/(8n+5) */
      
    mpf_sub(ftb[i], fta[i], ftc[i]);	/*  4/(8n+1) -  2/(8n+4)  - 1/(8n+5)  */

    mpf_add_ui(fta[i],B[i],6);	        /*  8n + 6 -> B + 6*/
    mpf_ui_div(ftc[i],1,fta[i]);	/*  1/(8n+6) */

    mpf_sub(fta[i], ftb[i], ftc[i]);	/*  4/(8n+1) - 2/(8n+4) - 1/(8n+5) - 1/(8n+6) */

    mpf_div(ftb[i],fta[i],A[i]);	/* M /16^n */


    /*
     * For Next Loop 
     */
    mpf_set(O[i],C[i]);
    mpf_add(C[i],O[i],ftb[i]);		/* O will be used as Pi(n-1) */


    /*
     *  Precision  check 
     */
    if ( !mpf_cmp(O[i],C[i] ) ) {     
      return ;                         /* precision is enough  */
    }

   
    for(k=0; k < pnum ; k++) {         /* 16^(n + pnum)  for next loop */
      mpf_mul_ui(fta[i],A[i],16);	      
      mpf_set(A[i],fta[i]);
    }

#ifdef VERBOSE 
    loopcounter++;
    if ( (loopcounter % loopdiv) == 0 ) {
      time(&t1);
      percent = (((loopcounter)/(fprec))*100.0);
      if ( percent < 98.0 ) {
	fprintf(stderr,"(Thread #%i)%.0f% (%d sec)\n",i,percent,t1-t0);
      }
    }
#endif

  }

}

main(int argc, char *argv[])
{
  pthread_t thread_context[PNUM];
  struct timeval t0, t1;
  int i,j;
  mpf_t pi, pi_tmp;



  if (argc>1) {
    if ( !strncmp(argv[1],"single",6) ) {
      pnum=1;
    }
    else if ( !strncmp(argv[1],"dual",4) ) {
      pnum=2;
    }
    else if ( !strncmp(argv[1],"quad",4) ) {
      pnum=4;
    }
    else if ( !strncmp(argv[1],"max",3) ) {
      pnum=PNUM;
    }
  }

  fprintf(stderr,"Number of Thread: %d\n",pnum);

  gettimeofday(&t0, NULL);

  dprec=DPREC;			/* decimal precision */
  loopdiv = dprec / 100;
  prec= bprec(dprec+10);  
  mpf_set_default_prec(prec);


  for(i=0; i < pnum ; i++) {
    pthread_create(&thread_context[i],NULL,thread_func,(void *)i);
  }
  for(i=0; i < pnum ; i++) {
    pthread_join ( thread_context[i], NULL );
  }
  mpf_init(pi);
  mpf_set_si(pi,0);

  mpf_init(pi_tmp);

  
  for(i=0;i<pnum;i++) {
    mpf_set(pi_tmp,pi);
    mpf_add(pi,C[i],pi_tmp);		/* O will be used as Pi(n-1) */
  }
  mpf_out_str(stdout,10,dprec + 10, pi);
  gettimeofday(&t1, NULL);
  
  fprintf(stderr,"%.3f sec\n",
	  ((t1.tv_sec-t0.tv_sec)*1000000 + (t1.tv_usec-t0.tv_usec))/1000000.0);
}
