import "./App.css"

function App() {
	return (
		<div className='container'>
			<div className='mx-auto w-[80vw] mt-5'>
				<div className='flex gap-10 items-center h-[30px]'>
					{/* Create task */}
					<div className='bg-lime-400 rounded-xl h-full flex items-center'>
						<a
							className='p-4'
							href='/new'
						>
							New task
						</a>
					</div>

					{/* Search task */}
					<div className='h-full'>
						<input
							className='w-[30vw] bg-slate-100 rounded-xl h-full px-4 mr-4'
							type='search'
							name='Task'
							id=''
							placeholder='Search task'
						/>
						<button>Search</button>
					</div>
				</div>
				{/* Task list */}
				<div className='w-[80vw] mt-10 bg-slate-100 rounded-xl p-2'>
					<table className='w-full'>
						<thead className='text-left'>
							<tr>
								<th>ID</th>
								<th>Task</th>
								<th>Description</th>
								<th>Done</th>
							</tr>
						</thead>
						<tbody>
							<tr className='border-t-2'>
								<td>8412398</td>
								<td>Cleaning</td>
								<td>Clean everything</td>
								<td>
									<input
										type='checkbox'
										name='done'
										id=''
									/>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	)
}

export default App
