
###############################################################################
#
# MassPayments
# Generates multiple payments from your PayPal Premier account or Business account to existing PayPal account holders.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MassPayments(Choreography):

    """
    Create a new instance of the MassPayments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/MassPayments')


    def new_input_set(self):
        return MassPaymentsInputSet()

    def _make_result_set(self, result, path):
        return MassPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MassPaymentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MassPayments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MassPaymentsInputSet(InputSet):
        """
        Set the value of the InputFile input for this choreography. ((required, any) An input file containing the payments to process. This data can either be in CSV or XML format. The format should be indicated using the InputFormat input. See Choreo documentation for schema details.)
        """
        def set_InputFile(self, value):
            InputSet._set_input(self, 'InputFile', value)

        """
        Set the value of the EmailSubject input for this choreography. ((optional, string) The subject line of the email that PayPal sends when the transaction is completed. This is the same for all recipients. Character length and limitations: 255 single-byte alphanumeric characters.)
        """
        def set_EmailSubject(self, value):
            InputSet._set_input(self, 'EmailSubject', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api-3t.paypal.com when running in production. Defaults to api-3t.sandbox.paypal.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the InputFormat input for this choreography. ((required, string) The type of input you are providing for this mass payment. Accepted values are "csv" or "xml". See Choreo documentation for expected schema details.)
        """
        def set_InputFormat(self, value):
            InputSet._set_input(self, 'InputFormat', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The API Password provided by PayPal.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Signature input for this choreography. ((required, string) The API Signature provided by PayPal.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)

        """
        Set the value of the User input for this choreography. ((required, string) The API Username provided by PayPal.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)

        """
        Set the value of the VaultFile input for this choreography. (The path to the vault file containing your payments in CSV or XML format. This can be used as an alternative to the InputFile input.)
        """


"""
A ResultSet with methods tailored to the values returned by the MassPayments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MassPaymentsResultSet(ResultSet):
        """
        Retrieve the value for the "Result" output from this choreography execution. (The MassPayment result from PayPal returned in the same format you've submitted.)
        """
        def get_Result(self):
            return self._output.get('Result', None)

class MassPaymentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MassPaymentsResultSet(response, path)
