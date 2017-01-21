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
        bus.start("127.255.255.255:2010"); // starts the bus on the default domain
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