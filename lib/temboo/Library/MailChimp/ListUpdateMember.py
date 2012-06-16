
###############################################################################
#
# ListUpdateMember
# Update information for a member of a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListUpdateMember(Choreography):

    """
    Create a new instance of the ListUpdateMember Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListUpdateMember')


    def new_input_set(self):
        return ListUpdateMemberInputSet()

    def _make_result_set(self, result, path):
        return ListUpdateMemberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUpdateMemberChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListUpdateMember
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListUpdateMemberInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EmailAddress input for this choreography. ((required, string) The current email address for the subscriber you want to update.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the EmailType input for this choreography. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        def set_EmailType(self, value):
            InputSet._set_input(self, 'EmailType', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The id of the list that the existing subsbriber belongs to.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the Merge1 input for this choreography. ((optional, string) Corresponds to the first merge var field defined in your account.)
        """
        def set_Merge1(self, value):
            InputSet._set_input(self, 'Merge1', value)

        """
        Set the value of the Merge2 input for this choreography. ((optional, string) Corresponds to the second merge var field defined in your account.)
        """
        def set_Merge2(self, value):
            InputSet._set_input(self, 'Merge2', value)

        """
        Set the value of the Merge3 input for this choreography. ((optional, string) Corresponds to the third merge var field defined in your account.)
        """
        def set_Merge3(self, value):
            InputSet._set_input(self, 'Merge3', value)

        """
        Set the value of the Merge4 input for this choreography. ((optional, string) Corresponds to the fourth merge var field defined in your account.)
        """
        def set_Merge4(self, value):
            InputSet._set_input(self, 'Merge4', value)

        """
        Set the value of the NewEmail input for this choreography. ((optional, multiline) Set this to update the email address of a subscriber.)
        """
        def set_NewEmail(self, value):
            InputSet._set_input(self, 'NewEmail', value)

        """
        Set the value of the ReplaceInterests input for this choreography. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_ReplaceInterests(self, value):
            InputSet._set_input(self, 'ReplaceInterests', value)


"""
A ResultSet with methods tailored to the values returned by the ListUpdateMember choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListUpdateMemberResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Mailchimp. Returns the string "true" for success and "false" for failures.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListUpdateMemberChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUpdateMemberResultSet(response, path)
