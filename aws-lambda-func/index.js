const stripe = require('stripe')('sk_test_51NRvW6BltQszbZOvUk3kHToUsIOfX6zn6YKzFb800AEKd0TQS1lhKvNj1coj9kcUl8GfJKUfLn5ouheuNBvImCT2004eMEWa1U');

exports.handler = async (event) => {
    try {
        const session = await stripe.checkout.sessions.create({
            payment_method_types: ['card'],
            line_items: [{
                price_data: {
                    currency: 'usd',
                    product_data: {
                        name: 'Donation',
                    },
                    unit_amount: 500, // e.g., $5.00, change as necessary
                },
                quantity: 1,
            }],
            mode: 'payment',
            success_url: 'https://yourdomain.com/success', // Update with your success URL
            cancel_url: 'https://yourdomain.com/cancel', // Update with your cancel URL
        });

        return {
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*', // Adjust based on your needs
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sessionId: session.id }),
        };
    } catch (error) {
        console.error(error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message }),
        };
    }
};