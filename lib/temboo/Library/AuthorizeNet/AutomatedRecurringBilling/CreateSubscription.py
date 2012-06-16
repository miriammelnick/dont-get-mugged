
###############################################################################
#
# CreateSubscription
# Creates a new subscription and sets up a recurring payment for the subscription.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateSubscription(Choreography):

    """
    Create a new instance of the CreateSubscription Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/AutomatedRecurringBilling/CreateSubscription')


    def new_input_set(self):
        return CreateSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return CreateSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSubscriptionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateSubscription
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateSubscriptionInputSet(InputSet):
        """
        Set the value of the RequestXML input for this choreography. ((optional, xml) Use this input to bybass single element inputs and submit your own XML for the request. See Authorize.net for information on the correct schema.)
        """
        def set_RequestXML(self, value):
            InputSet._set_input(self, 'RequestXML', value)

        """
        Set the value of the APILoginId input for this choreography. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        def set_APILoginId(self, value):
            InputSet._set_input(self, 'APILoginId', value)

        """
        Set the value of the AccountNumber input for this choreography. ((conditional, integer) The account number when a banking account payment is specified.)
        """
        def set_AccountNumber(self, value):
            InputSet._set_input(self, 'AccountNumber', value)

        """
        Set the value of the AccountType input for this choreography. ((conditional, string) The account type to use when a banking account payment is specified. Accepted values are: checking, businessChecking, and savings.)
        """
        def set_AccountType(self, value):
            InputSet._set_input(self, 'AccountType', value)

        """
        Set the value of the Amount input for this choreography. ((required, decimal) The amount to bill the customer for each recurring payment.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the BankName input for this choreography. ((conditional, string) The bank name associated with the bank account number specified for a bank account payment.)
        """
        def set_BankName(self, value):
            InputSet._set_input(self, 'BankName', value)

        """
        Set the value of the BillingAddress input for this choreography. ((optional, string) The street address associated with the billing address.)
        """
        def set_BillingAddress(self, value):
            InputSet._set_input(self, 'BillingAddress', value)

        """
        Set the value of the BillingCity input for this choreography. ((optional, string) The city associated with the billing address.)
        """
        def set_BillingCity(self, value):
            InputSet._set_input(self, 'BillingCity', value)

        """
        Set the value of the BillingCompany input for this choreography. ((optional, string) The company associated with the billing address.)
        """
        def set_BillingCompany(self, value):
            InputSet._set_input(self, 'BillingCompany', value)

        """
        Set the value of the BillingCountry input for this choreography. ((optional, string) The country associated with the billing address.)
        """
        def set_BillingCountry(self, value):
            InputSet._set_input(self, 'BillingCountry', value)

        """
        Set the value of the BillingFirstName input for this choreography. ((required, string) The first name associated with the billing address.)
        """
        def set_BillingFirstName(self, value):
            InputSet._set_input(self, 'BillingFirstName', value)

        """
        Set the value of the BillingLastName input for this choreography. ((required, string) The last name associated with the billing address.)
        """
        def set_BillingLastName(self, value):
            InputSet._set_input(self, 'BillingLastName', value)

        """
        Set the value of the BillingState input for this choreography. ((optional, string) The state associated with the billing address.)
        """
        def set_BillingState(self, value):
            InputSet._set_input(self, 'BillingState', value)

        """
        Set the value of the BillingZipCode input for this choreography. ((optional, string) The zip code associated with the billing address.)
        """
        def set_BillingZipCode(self, value):
            InputSet._set_input(self, 'BillingZipCode', value)

        """
        Set the value of the CardCode input for this choreography. ((conditional, integer) The 3 digit security code of the credit card.)
        """
        def set_CardCode(self, value):
            InputSet._set_input(self, 'CardCode', value)

        """
        Set the value of the CardNumber input for this choreography. ((conditional, integer) The credit card number for the recurring payment. Required unless a bank account payment is used.)
        """
        def set_CardNumber(self, value):
            InputSet._set_input(self, 'CardNumber', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) The description of the subscription. 255 max characters.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the ECheckType input for this choreography. ((conditional, string) The type of electronic check transaction used for the subscription. Acceptable values are: PPD or WEB. Required if bank payment is used.)
        """
        def set_ECheckType(self, value):
            InputSet._set_input(self, 'ECheckType', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) The email address of the customer)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ExpirationDate input for this choreography. ((optional, date) The 4 digit expiration date of the credit card. Required unless a bank account payment is used.)
        """
        def set_ExpirationDate(self, value):
            InputSet._set_input(self, 'ExpirationDate', value)

        """
        Set the value of the FaxNumber input for this choreography. ((optional, string) The fax number of the customer.)
        """
        def set_FaxNumber(self, value):
            InputSet._set_input(self, 'FaxNumber', value)

        """
        Set the value of the Id input for this choreography. ((optional, string) The merchant assigned customer id.)
        """
        def set_Id(self, value):
            InputSet._set_input(self, 'Id', value)

        """
        Set the value of the InvoiceNumber input for this choreography. ((optional, string) The merchant assigned invoice number for the subscription.)
        """
        def set_InvoiceNumber(self, value):
            InputSet._set_input(self, 'InvoiceNumber', value)

        """
        Set the value of the Length input for this choreography. ((optional, integer) Measurement of time for the frequency of billing. Associated with 'Unit'. Defaults to 1. Use 1-12 for unit months or 7-365 for unit days.)
        """
        def set_Length(self, value):
            InputSet._set_input(self, 'Length', value)

        """
        Set the value of the NameOnAccount input for this choreography. ((conditional, string) The name on the bank account. Required unless credit card payment is used.)
        """
        def set_NameOnAccount(self, value):
            InputSet._set_input(self, 'NameOnAccount', value)

        """
        Set the value of the PhoneNumber input for this choreography. ((optional, string) The phone number of the customer.)
        """
        def set_PhoneNumber(self, value):
            InputSet._set_input(self, 'PhoneNumber', value)

        """
        Set the value of the RefId input for this choreography. ((optional, string) The merchant-assigned reference ID for the request. If specified, it will be returned in the response from authorize.net.)
        """
        def set_RefId(self, value):
            InputSet._set_input(self, 'RefId', value)

        """
        Set the value of the RoutingNumber input for this choreography. ((conditional, integer) The routing number associated with the bank account payment. Required unless a credit payment is specified.)
        """
        def set_RoutingNumber(self, value):
            InputSet._set_input(self, 'RoutingNumber', value)

        """
        Set the value of the ShippingAddress input for this choreography. ((optional, string) The street address associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingAddress(self, value):
            InputSet._set_input(self, 'ShippingAddress', value)

        """
        Set the value of the ShippingCity input for this choreography. ((optional, string) The city associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingCity(self, value):
            InputSet._set_input(self, 'ShippingCity', value)

        """
        Set the value of the ShippingCompany input for this choreography. ((optional, string) The company associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingCompany(self, value):
            InputSet._set_input(self, 'ShippingCompany', value)

        """
        Set the value of the ShippingCountry input for this choreography. ((optional, string) The country associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingCountry(self, value):
            InputSet._set_input(self, 'ShippingCountry', value)

        """
        Set the value of the ShippingFirstName input for this choreography. ((optional, string) The first name associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingFirstName(self, value):
            InputSet._set_input(self, 'ShippingFirstName', value)

        """
        Set the value of the ShippingLastName input for this choreography. ((optional, string) The last name associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingLastName(self, value):
            InputSet._set_input(self, 'ShippingLastName', value)

        """
        Set the value of the ShippingState input for this choreography. ((optional, string) The state associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingState(self, value):
            InputSet._set_input(self, 'ShippingState', value)

        """
        Set the value of the ShippingZipCode input for this choreography. ((optional, string) The zip code associated with the shipping address. Used when the shipping and billing address are different.)
        """
        def set_ShippingZipCode(self, value):
            InputSet._set_input(self, 'ShippingZipCode', value)

        """
        Set the value of the StartDate input for this choreography. ((required, date) The date that the subscription and billing begin. Formatted like YYYY-MM-DD.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the SubscriptionName input for this choreography. ((optional, string) The merchant assigned name for the subscription. 50 max characters.)
        """
        def set_SubscriptionName(self, value):
            InputSet._set_input(self, 'SubscriptionName', value)

        """
        Set the value of the TotalOccurrences input for this choreography. ((optional, integer) Number of billing occurrences or payments for the subscription. Defaults to 9999 which means the subscription will be ongoing.)
        """
        def set_TotalOccurrences(self, value):
            InputSet._set_input(self, 'TotalOccurrences', value)

        """
        Set the value of the TransactionKey input for this choreography. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        def set_TransactionKey(self, value):
            InputSet._set_input(self, 'TransactionKey', value)

        """
        Set the value of the TrialAmount input for this choreography. ((conditional, decimal) The amount to be charged for a payment during a trial period. Required when TrialOccurances is specified. Defaults to 0.00.)
        """
        def set_TrialAmount(self, value):
            InputSet._set_input(self, 'TrialAmount', value)

        """
        Set the value of the TrialOccurrences input for this choreography. ((optional, integer) Number of billing occurrences or payments in the trial period. Defaults to 0.)
        """
        def set_TrialOccurrences(self, value):
            InputSet._set_input(self, 'TrialOccurrences', value)

        """
        Set the value of the Unit input for this choreography. ((optional, string) Unit of time between billing cycles. Used in association with interval 'Length'. Values can be 'months' or 'days'. Defaults to 'months'.)
        """
        def set_Unit(self, value):
            InputSet._set_input(self, 'Unit', value)


"""
A ResultSet with methods tailored to the values returned by the CreateSubscription choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateSubscriptionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Authorize.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSubscriptionResultSet(response, path)
