import java.awt.geom.Point2D;

/**
 * Created by renando on 18/01/17.
 */
public class Reconnaissance {

    public static int reconnaissance(Stroke listePoint, String[] listeCoor) {
        listePoint.normalize();
        int result = 0;
        int cpt = 0;


        for (Point2D.Double point : listePoint.getPoints()) {

            String x;
            String y;
            x = listeCoor[cpt].split(",")[0];
            y = listeCoor[cpt].split(",")[1];

            Double x1 = Double.parseDouble(x);
            Double y1 = Double.parseDouble(y);

            String x2 = String.valueOf(point.getX());
            String y2 = String.valueOf(point.getY());

            Double x3 = Double.parseDouble(x2);
            Double y3 = Double.parseDouble(y2);


            result += (int) Math.sqrt((Math.pow(x1 - x3, 2) + Math.pow(y1 - y3, 2)));
            cpt++;
        }
        System.out.println(result);
        return result;
    }


    public static String comparaison(int rond, int carre, int trait, int z) {
        String result = null;
        if(!isCorrect(rond) && !isCorrect(carre) &&!isCorrect(trait) &&!isCorrect(z) )
        {
            result="ERROR";
        }
        else if ((carre < rond) && (carre < trait) && (carre < z)) {
            result="RECTANGLE";
        } else if ((rond < carre) && (rond < trait) && (rond < z)) {
            result="ROND";
        } else if ((trait < carre) && (trait < rond) && (trait < z)) {
            result="TRAIT";
        } else if ((z < carre) && (z < rond) && (z < trait)) {
            result="Z";
        }
        else{
            result="ERROR";
        }
    return result;
    }

    public static boolean isCorrect(int forme){
        boolean result = true;
        if(forme > 1000){
            result = false;
        }
        return result;
    }
}
