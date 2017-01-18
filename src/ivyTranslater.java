import fr.dgac.ivy.Ivy;
import fr.dgac.ivy.IvyClient;
import fr.dgac.ivy.IvyException;
import fr.dgac.ivy.IvyMessageListener;

class ivyTranslater implements IvyMessageListener {

    private final Ivy bus;
    private String argument;

    ivyTranslater() throws IvyException {
        // initialization, name and ready message
        bus = new Ivy("IvyTranslater", "Geste", null);
        // classical subscription
        bus.bindMsg("sra5 Parsed=(.*) Confidence", this);
        // inner class subscription ( think awt )
        bus.bindMsg("^Bye$", (client, args) -> {
            // leaves the bus, and as it is the only thread, quits
            bus.stop();
        });
        bus.start("127.255.255.255:2010"); // starts the bus on the default domain
    }

    // callback associated to the "Hello" messages"
    void recevoire(Panel panel) throws IvyException {
        panel.stroke = new Stroke();
        bus.bindMsg("^coord=(.*)", (client, args) -> {
            if (args[0] != null) {
                panel.stroke = new Stroke();
                String[] listeCoor = args[0].split(";");
                String x;
                String y;
                for (String coor : listeCoor) {
                    x = coor.split(",")[0].replace(".0", "");
                    y = coor.split(",")[1].replace(".0", "");
                    panel.getStroke().addPoint(Integer.parseInt(x), Integer.parseInt(y));
                }
                panel.repaint();


            }
        });
    }

    void sendMsg(String msg) {
        try {
            bus.sendMsg(msg);
        } catch (IvyException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void receive(IvyClient ivyClient, String[] strings) {

    }
}