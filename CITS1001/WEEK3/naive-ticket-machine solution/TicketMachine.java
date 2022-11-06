/**
 * TicketMachine models a naive ticket machine that issues
 * flat-fare tickets.
 * The price of a ticket is specified via the constructor.
 * It is a naive machine in the sense that it trusts its users
 * to insert enough money before trying to print a ticket.
 * It also assumes that users enter sensible amounts.
 *
 * @author David J. Barnes and Michael Kölling
 * @version 2016.02.29
 */
public class TicketMachine
{
    // The price of a ticket from this machine.
    private int price;
    // The amount of money entered by a customer so far.
    private int balance;
    // The total amount of money collected by this machine.
    private int total;

    /**
     * Create a machine that issues tickets of the given price.
     * Note that the price must be greater than zero, and there
     * are no checks to ensure this.
     */
    public TicketMachine(int cost)
    {
        if (cost > 0) {price = cost;}
        else          {price = 1000;} // if cost is negative, use a default price
        balance = 0;
        total = 0;
    }

    /**
     * Create a machine that issues tickets of a default price.
     */
    public TicketMachine()
    {
        // calls the other constructor with the argument 1000 
        this(1000); 
    }


    /**
     * Return the price of a ticket.
     */
    public int getPrice()
    {
        return price;
    }

    /**
     * Return the amount of money already inserted for the
     * next ticket.
     */
    public int getBalance()
    {
        return balance;
    }

    /**
     * Return the total amount of money collected.
     */
    public int getTotal()
    {
        return total;
    }

    /**
     * Discount the ticket price.
     * Don't allow the price to be increased, and don't let it go to zero.
     */
    public void discount(int amount)
    {
        if (0 < amount && amount < price)
           price -= amount;
    }

    /**
     * Display the current ticket price.
     */
    public void showPrice()
    {
        System.out.println("The price of a ticket is " + price + " cents");
    }

    /**
     * Receive an amount of money from a customer.
     */
    public void insertMoney(int amount)
    {
        if (amount > 0) {balance += amount;}
        else            {System.out.println("Can't insert negative money: " + amount);}
    }

    /**
     * Print a ticket.
     * Update the total collected and reduce the balance to zero.
     * Three modifications have been made: 
     * - check that the balance is adequate to buy a ticket 
     * - subtract price from balance 
     * - add price to total
     */
    public void printTicket()
    {
        if (balance < price)
        {
            System.out.println("Not enough money to buy a ticket: need " + 
                               (price - balance) + " cents more");
        }
        else
        {
            // Simulate the printing of a ticket.
            System.out.println("##################");
            System.out.println("# The BlueJ Line");
            System.out.println("# Ticket");
            System.out.println("# " + price + " cents.");
            System.out.println("##################");
            System.out.println();

            // Update the total collected.
            total += price;
            // Reduce the balance.
            balance -= price;
        }
    }
}
