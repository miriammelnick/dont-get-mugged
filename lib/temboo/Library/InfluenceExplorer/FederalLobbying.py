
###############################################################################
#
# FederalLobbying
# Obtain detailed lobbying information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FederalLobbying(Choreography):

    """
    Create a new instance of the FederalLobbying Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/FederalLobbying')


    def new_input_set(self):
        return FederalLobbyingInputSet()

    def _make_result_set(self, result, path):
        return FederalLobbyingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FederalLobbyingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FederalLobbying
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FederalLobbyingInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Amount input for this choreography. ((optional, string) Enter the amount of dollars spent on lobbying.  Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the ClientParentOrganization input for this choreography. ((optional, string) Specify a full-text search of a client's parent organizationfor.)
        """
        def set_ClientParentOrganization(self, value):
            InputSet._set_input(self, 'ClientParentOrganization', value)

        """
        Set the value of the ClientSearch input for this choreography. ((optional, string) Enter the name of the client for whom this lobbyist is working. This parameter executes a full-text search.)
        """
        def set_ClientSearch(self, value):
            InputSet._set_input(self, 'ClientSearch', value)

        """
        Set the value of the FilingType input for this choreography. ((optional, string) Specify the type of filing as identified by CRP.  Example: n, for non-self filer parent.  For more info, go here: http://data.influenceexplorer.com/api/lobbying/)
        """
        def set_FilingType(self, value):
            InputSet._set_input(self, 'FilingType', value)

        """
        Set the value of the LobbyistSearch input for this choreography. ((optional, string) Specify a full-text search of a lobbyist's name.)
        """
        def set_LobbyistSearch(self, value):
            InputSet._set_input(self, 'LobbyistSearch', value)

        """
        Set the value of the RegistrantSearch input for this choreography. ((optional, string) Specify a full-text search of an organization or a person, who is fling the lobbyist registration.)
        """
        def set_RegistrantSearch(self, value):
            InputSet._set_input(self, 'RegistrantSearch', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TransactionID input for this choreography. ((optional, string) Enter the report ID given by the Senate Office of Public Records.)
        """
        def set_TransactionID(self, value):
            InputSet._set_input(self, 'TransactionID', value)

        """
        Set the value of the TransactionType input for this choreography. ((optional, string) Enter the type of filing as reported by the Senate Office of Public Records. See here for additional info: http://assets.transparencydata.org.s3.amazonaws.com/docs/transaction_types-20100402.csv)
        """
        def set_TransactionType(self, value):
            InputSet._set_input(self, 'TransactionType', value)

        """
        Set the value of the YearFiled input for this choreography. ((optional, string) Specify the year in which a registration was filed. Use the following format: yyyy. Example: 2011. Logical OR is also possible by using the | (pipe) symbol.  Example: 2008|2012.)
        """
        def set_YearFiled(self, value):
            InputSet._set_input(self, 'YearFiled', value)


"""
A ResultSet with methods tailored to the values returned by the FederalLobbying choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FederalLobbyingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FederalLobbyingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FederalLobbyingResultSet(response, path)
